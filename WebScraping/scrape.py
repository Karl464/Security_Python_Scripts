#!/usr/bin/Python 3

"""
Simple scrape service 1
Use this script to scrape information from web site
Note:
deploy soup test.html on localhost or change FQDNS to other site of your preference
"""

from bs4 import BeautifulSoup
import requests as req

resp = req.get("http://localhost/souptest.html")  #change to your desire FQDNS

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)

#prints the names of all HTML tags.
print("\n---------------prints the names of all HTML tags.---------------")
for child in soup.recursiveChildGenerator():
    if child.name:
        print(child.name)

print("\n---------------prints root_childs:---------------")
root_childs = [e.name for e in soup.children if e.name is not None]
print(root_childs)

print("\n---------------prints descendants:---------------")
descendants = [e.name for e in soup.descendants if e.name is not None]
print(descendants)
