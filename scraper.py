import requests
import csv
import pickle
import sys
from bs4 import BeautifulSoup

urlfile = csv.writer(open("rawdata.csv",'w'))

politicians = ['obama','clinton','biden','bush','mccain','romney','palin','bloomeberg','rice','christie','michelle-obama']

index_url = 'http://douthat.blogs.nytimes.com/?s='
urls = []

for politician in politicians:
	webpage = index_url + politician
	response = requests.get(webpage)
	soup = BeautifulSoup(response.text, 'html.parser')
	urls = urls + [a.attrs.get('href') for a in soup.findAll('a', {'class' : 'entry-title-link'})]

urlfile.writerow(urls)