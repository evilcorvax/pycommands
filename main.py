import sys
import os
import requests

from bs4 import BeautifulSoup

portal = "https://habr.com/"
hubs_dict = {"Python":"python/"}
lang = "ru/hub/"

portal_page = "page"
current_page_num = 1

html_page = requests.get(portal+lang+hubs_dict.get("Python")+portal_page+str(current_page_num))
dasm_page = BeautifulSoup(html_page.text, "html.parser")
r_count = 1
for element in dasm_page.find_all("div",{"class":"tm-article-snippet"}):
    for info in element.find_all("h2"):
        for title in info.find_all("a", href=True):
            print("=================Result", r_count)
            print(title["href"])
            print(title.span)
            print('==================')
            r_count+=1

# print(dasm_page.title)