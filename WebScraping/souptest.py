#!/usr/bin/Python 3

"""
Simple html reader
Use this script to scrape information from html file.
make use of souptest.html or change to your choice file

Require:
pip install beautifulsoup4
pip install lxml
"""
from bs4 import BeautifulSoup

with open("souptest.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.h2)
    print(soup.head)
    print(soup.li)

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

