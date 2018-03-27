import urllib.request
from bs4 import BeautifulSoup
import ssl
import csv

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Parsed the html
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
data = list()
l = list()

csv_file = open('transdformed.csv' , 'w')
writer = csv.writer(csv_file)

table = soup.findAll("table", "wikitable sortable")[1]

tr = table.find("tr")
th = tr.findAll("th")

l.append(th[0].text.strip())
l.append(th[1].text.strip())
l.append(th[2].text.strip())
l.append(th[3].text.strip())
l.append(th[4].text.strip())
l.append(th[5].text.strip())

data.append(l)

rows = table.findAll("tr")[1:]

for row in rows:
    lst = list()
    winning_team = list()
    losing_team = list()
    venue = list()

    columns = row.find_all('td')
    try:
        if not (columns[4].find_all('span')[1].text.strip() == "To be determined (TBD)"):
            lst.append(columns[0].find_all('span')[1].text.strip())
            lst.append(columns[1].find_all('span')[1].text.split()[2])

            wteam = columns[2].find_all('span')[0].text.split()
            for i in range(0,len(wteam)-1):
                winning_team.append(wteam[i])
            lst.append(" ".join(winning_team))

            score = columns[3].find_all('span')[1].text.split("(")
            score = "".join(score)
            score = score.split(")")
            score = "".join(score)
            lst.append(score)

            lteam = columns[4].find_all('span')[0].text.split()
            for i in range(0,len(lteam)-1):
               losing_team.append(lteam[i])
            lst.append(" ".join(losing_team))

            v = columns[5].find_all('span')[0].text.split()
            for i in range(0, len(v) - 1):
                venue.append(v[i])
            lst.append(" ".join(venue))

            data.append(lst)

    except:
        break

for row in data:
    writer.writerow(row)
csv_file.close()