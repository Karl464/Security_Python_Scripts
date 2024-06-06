#!/usr/bin/Python 3

"""
Use this script to scrape web pages

Require:
pip install requests
pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("http://localhost/souptest.html")

print(page.status_code)
#print(page.content)   #Raw data, not beutifull

soup = BeautifulSoup(page.content, 'html.parser') #Now change to beutifull data

print(soup)
#print(soup.prettify())
#print(list(soup.children))

[type(item) for item in list(soup.children)]

for item in list(soup.children):
    u_t=type(item)
    #print(u_t) 

fin=soup.findAll('a')    # extract all items ("headers") with the character “a.” 
fin=soup.find('a')          # extract one line of items with the character “a.” 
fin=soup.findAll('p')   # extract all items with the character “p.” paragraphs 
#print(fin)

#print url from a reference
for url in soup.find_all('a'):
    print(url.get('href'))

#print only text
print(soup.get_text())

#We can access the soup.body to get the body section. Then, grab the .text from there using the following sequence of commands:
body = soup.body
for paragraph in body.find_all('a'):
    print(paragraph.text)

#The best method to practice with this tool is to create a web page, and then query the different parameters to yield a result.



