import re
from requests_html import HTMLSession
import csv
url = "https://auburntigers.com/staff-directory"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
emailSet = set()

session = HTMLSession()

r = session.get(url)

r.html.render()

for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    emailSet.add(re_match.group())

#print(emailSet)

with open('emails.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= ['email'])

    writer.writeheader()
    for i in emailSet:
        writer.writerow({'email': i})
