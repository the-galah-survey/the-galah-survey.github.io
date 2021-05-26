import json

text=open("people.json",'r')
x=text.read()

galah_people=json.loads(x)

with open("../../people.md", 'w') as people_md:
    people_md.write("""---
title: People
subtitle: The humans behind the GALAH Survey
""")
    people_md.write("executive-board:\n")
    for person in [p for p in galah_people if 'SMG' in p['tag']]:
        person_entry = []
        person_entry.append(f"  - name: {person['name']}")
        person_entry.append(f"    affiliation: {person['affiliation']}")
        if 'description' in person:
            person_entry.append(f"    desc: {person['description']}")
        if 'website' in person:
            person_entry.append(f"    website: {person['website']}")
        if 'twitter' in person:
            person_entry.append(f"    twitter: https://twitter.com/{person['twitter']}")
        if 'github' in person:
            person_entry.append(f"    github: https://github.com/{person['github']}")
        if 'email' in person:
            person_entry.append(f"    email: {person['email']}")
        person_entry.append(f"    img: /assets/img/people/{'-'.join(person['name'].lower().split())}.jpg")
        person_entry.append("\n")
        people_md.write(("\n".join(person_entry))[:-1])
        

    people_md.write("""---

## Survey Management Group

These people are currently heading GALAH.

{% include list-circles.html items=page.executive-board %}""")
