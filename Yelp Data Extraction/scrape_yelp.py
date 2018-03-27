from urllib import request
from bs4 import BeautifulSoup
import csv
import re
import time
import random
import urllib
import ssl
from collections import OrderedDict


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

rest_file = open('restaurant.csv' , 'w', newline='')
writer_rest = csv.writer(rest_file)
author_file = open('author.csv' , 'w', newline='')
writer_author = csv.writer(author_file)
review_file = open('review.csv' , 'w', newline='')
writer_review = csv.writer(review_file)

restlist = list()

l1 = list()
l1.append("restaurantID")
l1.append("name")
l1.append("location")
l1.append("reviewcount")
l1.append("rating")
l1.append("categories")
l1.append("address")
l1.append("Hours")
l1.append("GoodforKids")
l1.append("AcceptsCreditCards")
l1.append("Parking")
l1.append("Attire")
l1.append("GoodforGroups")
l1.append("PriceRange")
l1.append("TakesReservations")
l1.append("Delivery")
l1.append("Takeout")
l1.append("WaiterService")
l1.append("OutdoorSeating")
l1.append("WiFi")
l1.append("GoodFor")
l1.append("Alcohol")
l1.append("NoiseLevel")
l1.append("Ambience")
l1.append("HasTV")
l1.append("Caters")
l1.append("WheelchairAccessible")
l1.append("webSite")
l1.append("phoneNumber")
restlist.append(l1)




authorlist = list()
l2 = list()
l2.append("authorID")
l2.append("name")
l2.append("location")
l2.append("reviewCount")
l2.append("friendCount")
l2.append("photoCount")
authorlist.append(l2)


reviewlist = list()
l3= list()
l3.append("reviewID")
l3.append("businessID")
l3.append("reviewerID")
l3.append("date")
l3.append("reviewContent")
l3.append("rating")
l3.append("usefulCount")
l3.append("coolCount")
l3.append("funnyCount")
reviewlist.append(l3)

pages = range(0,70)
count = 0
for each in pages:
	web_page = request.urlopen("https://www.yelp.com/search?find_loc=60654&start={}0&cflt=restaurants".format(each),context=ctx).read()
	soup = BeautifulSoup(web_page, 'html.parser')

	restaurants = soup.findAll('div', attrs={'class':re.compile(r'^search-result natural-search-result')})

	extracted = [] # a list of tuples
	try:
		for r in restaurants:
			img = ''
			yelpPage = ''
			title = ''
			restrating = ''
			addr = ''
			phone = ''
			categories = ''
			website = ''

			attributes = OrderedDict()

			attributes['Today'] = "Null"
			attributes['Good for Kids'] = "Null"
			attributes['Accepts Credit Cards'] = "Null"
			attributes['Parking'] = "Null"
			attributes['Attire'] = "Null"
			attributes['Good for Groups'] = "Null"
			attributes['Price range'] = "Null"
			attributes['Takes Reservations'] = "Null"
			attributes['Delivery'] = "Null"
			attributes['Take-out'] = "Null"
			attributes['Waiter Service'] = "Null"
			attributes['Outdoor Seating'] = "Null"
			attributes['Wi-Fi'] = "Null"
			attributes['Good For'] = "Null"
			attributes['Alcohol'] = "Null"
			attributes['Noise Level'] = "Null"
			attributes['Ambience'] = "Null"
			attributes['Has TV'] = "Null"
			attributes['Caters'] = "Null"
			attributes['Wheelchair Accessible'] = "Null"


			img = r.div('div', {'class':'media-avatar'})[0].img['src']
			restaurantid = r["data-biz-id"]
			reviewcount = r.find('span', {'class': "review-count rating-qualifier"}).getText().split()[0]
			title = r.find('a', {'class':'biz-name'}).getText().strip()
			yelpPage = r.find('a', {'class':['biz-name','js-analytics-click']})['href']
			categories = r.findAll('span', {'class':'category-str-list'})
			categories = ','.join([c.getText().strip() for c in categories if c.getText().strip()])
			addr = r.find('div', {'class':'secondary-attributes'}).address.getText().strip()
			r2 = r.find('div', {'class': "biz-rating biz-rating-large clearfix"}).find('div')
			restrating = r2['title'].split()[0]


			zipcode = addr.strip()[-5:]
			if zipcode == "60654":

				web_page2 = request.urlopen(urllib.parse.urljoin('http://www.yelp.com', yelpPage),context=ctx).read()
				soup2 = BeautifulSoup(web_page2, 'html.parser')

				hours = soup2.find('tbody')
				all_days = hours.findAll('th')

				hours_csv = ''

				for each in all_days:
					day = str(each).split('>')[1].split('<')[0]
					day_hours = each.find_next_sibling('td').text.strip()
					hours_csv += day + ' '
					hours_csv += day_hours + ' '



				location = soup2.find("strong", {"class": "street-address"})
				neighbourhood = location.find("address").getText(separator=" ").strip()
				neighbourhood += " Neighbourhood: "
				neighbourhood += soup2.find("strong", {"class": "street-address"}).find_next_sibling('span').text.strip()



				takes_res = soup2.findAll('dt', class_=['ywidget', 'ylist', 'short-def-list', 'attribute-key'])

				for each in takes_res:
					attributes[each.getText().strip()] = each.find_next_sibling('dd').text.strip()



				website = soup2.find('span', {'class':"biz-website"}).getText().split()[2]
				phone = soup2.find('span', {'class':'biz-phone'}).getText().strip()

				'''
				temp = soup2.find('div',{'class':['short-def-list','attribute-key']}).getText().strip().split('  ')
				temp = list(filter(None, temp))
				temp = [x for x in temp if not x.startswith(('\n'))]
				temp = [x[:-1] for x in temp]
				'''
				authors = soup2.findAll('div', {'class' : "review review--with-sidebar"})


				if (int(reviewcount.split()[0]) >= 20):

					count += 1
					for author in authors:
						lst = list()
						#authorid
						lst.append(author.find('a', {'class' : "user-display-name"})['href'].split("=")[1])
						#authorname
						lst.append(author.find('a', {'class' : "user-display-name"}).getText().strip())
						#authorlocation
						lst.append(author.find('li',{'class' : "user-location responsive-hidden-small"}).getText().strip())
						#reviewcount
						lst.append(int(author.find('li',{'class' : "review-count responsive-small-display-inline-block"}).getText().strip().split(" ")[0]))
						#friendcount
						lst.append(int(author.find('li',{'class' : "friend-count responsive-small-display-inline-block"}).getText().strip().split(" ")[0]))
						#photocount
						temp = author.find('li',{'class' : "photo-count responsive-small-display-inline-block"})
						if temp:
							lst.append(int(temp.getText().strip().split(" ")[0]))
						else:
							lst.append(0)
						authorlist.append(lst)


					reviews = soup2.findAll('div', {'class': "review review--with-sidebar"})
					for review in reviews:
						lst2 = list()

						#check if all ids are correct
						# review id
						lst2.append(review.find('div', {'class': "rateReview voting-feedback"})["data-review-id"])

						#business id (it is equal to the restaurant id right?)
						lst2.append(r["data-biz-id"])

						#reviewer id
						lst2.append(review.find('a', {'class': "user-display-name"})['href'].split("=")[1])

						#date
						lst2.append(review.find('span',{'class' : "rating-qualifier"}).getText().split()[0])

						# content
						lst2.append(review.find('div', {'class': "review-content"}).find('p').getText().strip())

						# rating
						r1 = review.find('div',{'class': "biz-rating biz-rating-large clearfix"}).find('div').find('div')
						lst2.append(r1['title'].split()[0])

						# usefulcount
						useful = review.find('a',{'class': "ybtn ybtn--small useful js-analytics-click"})
						tempu = useful.find('span', {'class': "count"}).getText().strip()
						if tempu != '':
							lst2.append(tempu)
						else:
							lst2.append(0)


						# coolcount
						cool = review.find('a', {'class': "ybtn ybtn--small cool js-analytics-click"})
						tempc = cool.find('span', {'class': "count"}).getText().strip()
						if tempc != '':
							lst2.append(tempc)
						else:
							lst2.append(0)


						# funnycount
						funny = review.find('a', {'class': "ybtn ybtn--small funny js-analytics-click"})
						tempf = funny.find('span', {'class': "count"}).getText().strip()
						if tempf != '':
							lst2.append(tempf)
						else:
							lst2.append(0)
						


						reviewlist.append(lst2)

					acceptcreditCards = attributes['Accepts Credit Cards']
					parking = attributes['Parking']
					attire = attributes['Attire']
					goodforgroups = attributes['Good for Groups']
					goodforkids = attributes['Good for Kids']
					takesreservations = attributes['Takes Reservations']
					delivery = attributes['Delivery']
					takeout = attributes['Take-out']
					waiterService = attributes['Waiter Service']
					outdoorSeating = attributes['Outdoor Seating']
					wifi = attributes['Wi-Fi']
					priceRange = attributes['Price range']
					goodFor = attributes['Good For']
					alcohol = attributes['Alcohol']
					noiselevel = attributes['Noise Level']
					ambience = attributes['Ambience']
					hastv = attributes['Has TV']
					caters = attributes['Caters']
					wheelchairAccessible = attributes['Wheelchair Accessible']


					lst3 = list()


					lst3.append(restaurantid)
					lst3.append(title)
					lst3.append(neighbourhood)
					lst3.append(reviewcount)
					lst3.append(restrating)
					lst3.append(categories)
					lst3.append(addr)
					lst3.append(hours_csv)
					lst3.append(goodforkids)
					lst3.append(acceptcreditCards)
					lst3.append(parking)
					lst3.append(attire)
					lst3.append(goodforgroups)
					lst3.append(priceRange)
					lst3.append(takesreservations)
					lst3.append(delivery)
					lst3.append(takeout)
					lst3.append(waiterService)
					lst3.append(outdoorSeating)
					lst3.append(wifi)
					lst3.append(goodFor)
					lst3.append(alcohol)
					lst3.append(noiselevel)
					lst3.append(ambience)
					lst3.append(hastv)
					lst3.append(caters)
					lst3.append(wheelchairAccessible)
					lst3.append(website)
					lst3.append(phone)

					restlist.append(lst3)

				print('count:', count)
				print('\nRest List:\n', restlist)
				print('\nReview List:\n', reviewlist)
				print('\nAuthor List:\n', authorlist)
				print()

				if count> 200:
					break

	except:
		continue



for row in restlist:
    writer_rest.writerow(row)
rest_file.close()

for row in authorlist:
    writer_author.writerow(row)
author_file.close()

for row in reviewlist:
    writer_review.writerow(row)
review_file.close()