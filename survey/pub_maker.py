# encode: utf-8
"""
Convert your ADS Libraries into the markdown publication pages.
"""

import os
import requests
import json
import re


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
    except KeyError:
        raise KeyError(r.text)
    return bibcodes


def get_pub_markdown(bibcodes):
    """
    """

    config = get_config()

    payload = {"bibcode": bibcodes,
               "sort": "date desc",
               "format": "* **[%T](%u)**<br/>%2M (%Y) %q **%V** %pp <small>([%X](https://arxiv.org/abs/%X); [doi:%d](https://doi.org/%d))</small>"}
    r = requests.post("https://api.adsabs.harvard.edu/v1/export/custom",
                      headers=config['headers'],
                      data=json.dumps(payload))
    # Get all the documents that are inside the library
    try:
        data = r.json()['export']
    except ValueError:
        raise ValueError(r.text)
    return data


def create_webpage(library_name, page_name, title, subtitle):
    bibcodes = get_bibcodes(library_name)
    markdown_list = get_pub_markdown(bibcodes)

    with open(page_name, 'w') as pub_md:
        pub_md.write(f"""---
layout: page
title: {title}
subtitle: {subtitle}
---

<!-- Do not edit this page directly. Instead use /pub_lists/pub_maker.py. -->
""")
        year = None
        for pub in markdown_list.split('\n')[:-1]:
            pub_year = pub.split("/abs/")[1][:4]

            # These are a bunch of needed fix for minor issues with formatting.
            pub = pub.replace(r"; [doi:](https://doi.org/)", "")
            pub = pub.replace(r"(https://arxiv.org/abs/); ", "")
            pub = pub.replace(r"MNRAS.tmp ****", "MNRAS")

            pub = re.sub(r" arXiv [*]{4} arXiv:[0-9]+.[0-9]+ ",
                         ' arXiv e-print ', pub)
            pub = pub.replace(r"$\sim$", "~")
            pub = pub.replace(r"$R$", "*R*")
            pub = pub.replace(r"[$\alpha/\rm Fe]$", "[α/Fe]")
            pub = pub.replace(r"$\alpha$", "α")
            pub = pub.replace(r"∼", "~")
            pub = pub.replace(r"$< -0.75$", "< −0.75")
            if (year is None) | (year != pub_year):
                year = pub_year
                pub_md.write(f"\n#### {year}\n")
            pub_md.write(pub + '\n')


if __name__ == '__main__':
    create_webpage(library_name='h8cKhLXSTaSOuZAy7phffg',
                   page_name="survey/external_publications.md",
                   title="Publications using GALAH",
                   subtitle="This page lists publications using GALAH data.")

    create_webpage(library_name='clbnJI34RXa4uEEqFC8I9g',
                   page_name="survey/galah_publications.md",
                   title="GALAH Survey publications",
                   subtitle="This page lists publications from the GALAH Survey team.")
