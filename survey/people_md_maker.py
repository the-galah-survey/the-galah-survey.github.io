import pandas as pd

def create_picture_entries(person):
    full_name = " ".join([person['first_name'], person['last_name']])
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
        contact_string.append(f'<a class="item-link" href="https://twitter.com/{twitter}" title="{full_name} on Twitter"><span class="fab fa-twitter"></span></a>')
    if not person[['website']].isna()[0]:
        website_link = person["website"]
        contact_string.append(f'<a class="item-link" href="{website_link}" title="Personal website of {full_name}"><span class="fas fa-home"></span></a>')
    if not person[['github']].isna()[0]:
        github_link = f"https://github.com/{person['github']}"
        contact_string.append(f'<a class="item-link" href="{github_link}" title="{full_name} on GitHub"><span class="fab fa-github"></span></a>')
    return "&#8201;".join(contact_string)

def main():
    galah_people = pd.read_json("survey/people.json")

    with open("survey/people.md", 'w') as people_md:
        people_md.write("""---
title: People
subtitle: The humans behind the GALAH Survey
""")
        # Add the builders and SMG
        for tag in ["smg", "builder"]:
            people_md.write(f"{tag}:\n")
            for *_, person in galah_people[galah_people['tag'] == tag].sort_values(['last_name', 'first_name'], key=lambda col: col.str.lower()).iterrows():
                person_entry = create_picture_entries(person)
                people_md.write(("\n".join(person_entry))[:-1])
        people_md.write("""---


### Survey Management Group

These people are currently heading GALAH.

{% include list-circles.html items=page.smg %}



### Builders

These people are GALAH Survey builders

{% include list-circles.html items=page.builder %}
""")
        people_md.write("""
### The entire team

All the members of the GALAH Survey

| Name | Affiliation | Contact |
| :------ |:--- | :--- |
""")
        for *_, person in galah_people.sort_values(['last_name', 'first_name'], key=lambda col: col.str.lower()).iterrows():
            person_entry = []
            person_name_field = " ".join(["|", person['first_name'], person['last_name']])
            
            
            description_str = []
            if person.tag == "smg":
                description_str.append("Survey&nbsp;Management&nbsp;Group")
            if person.tag == "builder":
                description_str.append("Survey&nbsp;Builder")
            if not person[['description']].isna()[0]:
                description_str.append(person['description'])
            
            if description_str:
                person_name_field = person_name_field + "<br/><small>(" + ",<br/>".join(description_str) + ")</small>"
        
            person_entry.append(person_name_field)
    
            if not person[['affiliation']].isna()[0]:
                person_entry.append(f"{person['affiliation']}")
            else:
                person_entry.append("")
            person_entry.append(create_contact_icons(person))
            person_entry.append("\n")
            people_md.write((" | ".join(person_entry)))
         
if __name__ == "__main__":   
    main()