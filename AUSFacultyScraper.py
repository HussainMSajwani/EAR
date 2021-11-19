from bs4 import BeautifulSoup
import requests
import pandas as pd


def untitle(s):
    if (s.startswith("Dr. ") or s.startswith("Ms. ") or s.startswith("Mr. ")):
        out = s[4:]
    else:
        out = s
    return out
names = []
titles = []

for page_index in range(1, 31):
    URL = f'https://www.aus.edu/faculty-hub?page={page_index}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")   
    profiles = soup.find_all("div", {"class": "views-row"})

    for profile in profiles:
        names.append(untitle(profile.find_all("div", {"class": "title"})[0].text.strip()))
        titles.append(profile.find_all("div", {"class": "position"})[0].text.strip())

df = pd.DataFrame({
    'name': names,
    'title': titles
})

df.to_csv('data/AUS/AUS_faculty.csv', index=False)