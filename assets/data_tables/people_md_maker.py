import pandas as pd

def create_picture_entries(person):
    full_name = " ".join([person['first_name'], person['last_name']])
    print(full_name)
    person_entry = []
    person_entry.append(f"  - name: {person['first_name']} {person['last_name']}")
    person_entry.append(f"    affiliation: {person['affiliation']}")
    if not person[['description']].isna()[0]:
        person_entry.append(f"    desc: {person['description']}")
    if not person[['website']].isna()[0]:
        person_entry.append(f"    website: {person['website']}")
    if not person[['twitter']].isna()[0]:
        person_entry.append(f"    twitter: https://twitter.com/{person['twitter']}")
    if not person[['github']].isna()[0]:
        person_entry.append(f"    github: https://github.com/{person['github']}")
    if not person[['email']].isna()[0]:
        person_entry.append(f"    email: {person['email']}")
    person_entry.append(f"    img: /assets/img/people/{'-'.join(full_name.lower().split())}.jpg")
    person_entry.append("\n")
    return person_entry


def create_contact_icons(person):
    contact_string = []
    full_name = " ".join([person['first_name'], person['last_name']])
    if not person[['email']].isna()[0]:
        email = person['email']
        contact_string.append(f'<a class="item-link" href="mailto:{email}" title="Email {full_name}"><span class="fas fa-envelope"></span></a>')
    if not person[['twitter']].isna()[0]:
        twitter = person['twitter']
        contact_string.append(f'<a class="item-link" href="https://twitter.com/{twitter}" title="Tweet {full_name}"><span class="fab fa-twitter"></span></a>')
#     if not person[['website']].isna()[0]:
#         person_entry.append(f"    website: {person['website']}")

#     if not person[['github']].isna()[0]:
#         person_entry.append(f"    github: https://github.com/{person['github']}")
    return " ".join(contact_string)


galah_people = pd.read_csv("/assets/data_tables/people.csv", sep='\t')

with open("/people.md", 'w') as people_md:
    people_md.write("""---
title: People
subtitle: The humans behind the GALAH Survey
""")

    ## Add the SMG
    people_md.write("smg:\n")
    for *_, person in galah_people[galah_people['tag'] == 'SMG'].sort_values('last_name').iterrows():
        person_entry = create_picture_entries(person)
        people_md.write(("\n".join(person_entry))[:-1])
    ## Add the builders
    people_md.write("builders:\n")
    for *_, person in galah_people[galah_people['tag'] == 'Builders'].sort_values('last_name').iterrows():
        person_entry = create_picture_entries(person)
        people_md.write(("\n".join(person_entry))[:-1])

    people_md.write("""---


### Survey Management Group

These people are currently heading GALAH.

{% include list-circles.html items=page.smg %}



### Builders

These people are GALAH Survey builders

{% include list-circles.html items=page.builders %}
""")
    people_md.write("""
### The entire team

All the members of the GALAH Survey

| Name | Affiliation | Contact |
| :------ |:--- | :--- |
""")
    for *_, person in galah_people.sort_values('last_name').iterrows():
        person_entry = []
        person_entry.append(" ".join(["|", person['first_name'], person['last_name']]))
        if not person[['affiliation']].isna()[0]:
            person_entry.append(f"{person['affiliation']}")
        else:
            person_entry.append("")
        person_entry.append(create_contact_icons(person))
        person_entry.append("\n")
        people_md.write((" | ".join(person_entry)))
