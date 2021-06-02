# encode: utf-8
"""
Convert your ADS Libraries into the markdown publication pages.
"""

import os
import requests
import pandas as pd
from urllib.parse import quote
import matplotlib.pyplot as plt
from pathlib import Path


def get_config():
    """
    Load ADS developer key from file
    :return: str
    """
    try:
        token = os.getenv('ADS_TOKEN')
    # try:
    #     with open(os.path.expanduser('~/.ads/dev_key')) as f:
    #         token = f.read().strip()
    except IOError:
        print('The script assumes you have your ADS developer token in the'
              'folder: {}'.format())

    return {
        'url': 'https://api.adsabs.harvard.edu/v1/biblib',
        'headers': {
            'Authorization': 'Bearer:{}'.format(token),
            'Content-Type': 'application/json',
        }
    }


def get_bibcodes(library_id):
    start = 0
    rows = 1000
    config = get_config()

    r = requests.get(
        '{}/libraries/{id}?start={start}&rows={rows}'.format(
            config['url'],
            id=library_id,
            start=start,
            rows=rows
        ),
        headers=config['headers']
    )
    # Get all the documents that are inside the library
    try:
        bibcodes = r.json()['documents']
    except ValueError:
        raise ValueError(r.text)
    return bibcodes


def get_title_str(pub):
    # This fixes up a bunch of minor formatting issues
    title_str = pub['title'][0]
    title_str = title_str.replace(r"$\sim$", "~").replace(r"$R$", "*R*").replace(
        r"[$\alpha/\rm Fe]$", "[α/Fe]").replace(r"$\alpha$", "α").replace(r"∼", "~").replace(r"$< -0.75$", "< −0.75")
    return title_str


def get_author_str(pub):
    # Different author formats depending on the number of authors
    if pub['author_count'] == 1:
        return f"{pub['author'][0].split(',')[0]}"
    if pub['author_count'] == 2:
        return f"{pub['author'][0].split(',')[0]} and {pub['author'][1].split(',')[0]}"
    if pub['author_count'] > 2:
        return f"{pub['author'][0].split(',')[0]} *et al.*"


def get_pub_vol_pp_str(pub):
    publication_str = pub['bibstem'][0]
    vol_str = ""
    pp_str = ""
    # Fixes for when there is no volume or page number
    if pub['bibstem'][0] != 'arXiv':
        vol_str = f"**{pub['volume']}**".replace("** **", "")
        pp_str = f"{pub['page'][0]}".replace(" ", "")
    return f"{publication_str} {vol_str} {pp_str}"


def get_doi_str(pub):
    if pub['doi'][0] == " ":
        return None
    return f"[doi:{pub['doi'][0]}](https://doi.org/{pub['doi'][0]})"


def get_arxiv_str(pub):
    arXiv_id = [i for i in pub['identifier'] if i.startswith("arXiv:")]
    if len(arXiv_id) == 0:
        return None
    return f"[{arXiv_id[0]}](https://arxiv.org/abs/{arXiv_id[0]})"


def link_str(doi_str, arxiv_str):
    if (doi_str is None) and (arxiv_str is None):
        return ""
    if (doi_str is None):
        return f"<small>({arxiv_str})</small>"
    if (arxiv_str is None):
        return f"<small>({doi_str})</small>"
    return f"<small>({doi_str}, {arxiv_str})</small>"


def create_webpage(library_id, md_pub_file, title, subtitle):
    config = get_config()
    bibcodes = get_bibcodes(library_id)

    r = requests.post("https://api.adsabs.harvard.edu/v1/search/bigquery",
                      params={"q": "*:*",
                              "fl": "bibcode,title,year,bibstem,author_count,volume,pub,page,issue,identifier,author,doi,date,doctype",
                              "rows": 2000},
                      headers={'Authorization': config['headers']['Authorization'],
                               'Content-Type': 'big-query/csv'},
                      data="bibcode\n" + "\n".join(bibcodes))
    doc_dict = r.json()['response']['docs']

    pub_df = pd.DataFrame(doc_dict)
    pub_df.fillna(value=" ", inplace=True)

    cwd = Path(__file__).parent
    img_name = f"{md_pub_file.split('.')[0].split('/')[1]}_number_papers.png"

    with open(md_pub_file, 'w') as pub_md:
        pub_md.write(f"""---
layout: page
title: {title}
subtitle: {subtitle}
---

<!-- Do not edit this page directly. Instead use /pub_lists/pub_maker.py. -->
""")
        # pub_md.write(f"This page collates the over {int(len(bibcodes)/10)*10} papers that have used GALAH Survey data.\n")
        pub_md.write(
            f"![Number of publications using GALAH](/survey/img/{img_name})\n")

        year_list = []
        article_list = []
        eprint_list = []
        for year, year_df in pub_df.sort_values('year', ascending=False).groupby("year", sort=False):
            year_list.append(int(year))
            year_counts = year_df['doctype'].value_counts()
            if 'article' in year_counts:
                article_list.append(year_counts['article'])
            else:
                article_list.append(0)
            if 'eprint' in year_counts:
                eprint_list.append(year_counts['eprint'])
            else:
                eprint_list.append(0)
            pub_md.write(f"#### {year}\n")
            for *_, pub in year_df.sort_values(['date', 'bibcode'], ascending=[False, True]).iterrows():
                markdown_str = "* "
                title_str = f"[**{get_title_str(pub)}**](https://ui.adsabs.harvard.edu/abs/{quote(pub['bibcode'])})"
                author_str = get_author_str(pub)
                year_str = f"({pub['year']})"
                publication_str = get_pub_vol_pp_str(pub)

                markdown_str = f"* {title_str}<br/>{author_str} {year_str} {publication_str} {link_str(get_doi_str(pub), get_arxiv_str(pub))}\n"

                pub_md.write(markdown_str)

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(year_list, article_list, tick_label=year_list,
           label='Refereed', color='pink')
    ax.bar(year_list, eprint_list, bottom=article_list,
           label='Non-refereed', color='C4')
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of publications")
    ax.set_title("Increasing use of the GALAH survey")
    ax.legend()

    # Get the Path object to save the image

    img_dir = Path.joinpath(cwd, "img")
    if not img_dir.exists():
        img_dir.mkdir(parents=True, exist_ok=True)

    img_location = Path.joinpath(img_dir, img_name)
    fig.savefig(img_location, bbox_inches='tight',
                dpi=400, transparent=False)
    # plt.show()


if __name__ == '__main__':
    create_webpage(library_id='h8cKhLXSTaSOuZAy7phffg',
                   md_pub_file="survey/external_publications.md",
                   title="Publications using GALAH data",
                   subtitle="This page lists publications using GALAH data.")

    create_webpage(library_id='clbnJI34RXa4uEEqFC8I9g',
                   md_pub_file="survey/galah_publications.md",
                   title="GALAH Survey team publications",
                   subtitle="This page lists publications from the GALAH Survey team.")
