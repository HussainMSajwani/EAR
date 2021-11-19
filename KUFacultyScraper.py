from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.ku.ac.ae/faculty-directory"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
blks = soup.find_all("div", {"class": "blk clear"})

undoctor = lambda name: name[4:] if name.startswith("Dr. ") else name 

df = pd.DataFrame({
    'name': [undoctor(blk.find_all("span", {"class": 'name'})[0].text) for blk in blks],
    'title': [blk.find_all("span", {"class": 'title'})[0].text for blk in blks],
    'department': [blk.find_all("span", {"class": 'department'})[0].text for blk in blks]
})

df.to_csv('data/KU.csv', index=False)