import pathlib
from os import getcwd
from bs4 import BeautifulSoup
import requests
import pandas as pd
from .utils import _faculty_untitle

class FacultyScholarScraper:
    """absstract class for faculty scrapers
    """
    def __init__(self, institute):
        self.institute = institute
        self.faculty_df = None
        self.data_dir = pathlib.Path(__file__).parent.parent / "data" / self.institute


    def scrape_faculty(self):
        """generate dataframe of faculty

        Returns:
            pd.DataFrame: faculty dataframe
        """
        return self.faculty_df

    def to_csv(self):
        """save CSV of self.faculty_df
        """
        if self.faculty_df is not None:
            self.faculty_df.to_csv(self.data_dir / f"{self.institute}_faculty.csv", index=False)

class KUScraper(FacultyScholarScraper):
    
    def __init__(self):
        institute = "KU"
        super().__init__(institute)
    
    def scrape_faculty(self):
        """Scrape KU faculty directory

        Returns:
            pd.DataFrame: KU faculty
        """
        URL = "https://www.ku.ac.ae/faculty-directory"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        blks = soup.find_all("div", {"class": "blk clear"})


        df = pd.DataFrame({
            'name': [_faculty_untitle(blk.find_all("span", {"class": 'name'})[0].text) for blk in blks],
            'title': [blk.find_all("span", {"class": 'title'})[0].text for blk in blks],
            'department': [blk.find_all("span", {"class": 'department'})[0].text for blk in blks]
        })
        self.faculty_df = df
        return df

class AUSScraper(FacultyScholarScraper):

    def __init__(self):
        institute = "AUS"
        super().__init__(institute)

    def scrape_faculty(self):
        names = []
        titles = []
        departments = []

        for page_index in range(1, 31):
            URL = f"https://www.aus.edu/faculty-hub?page={page_index}"
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")   
            profiles = soup.find_all("div", {"class": "views-row"})

            for profile in profiles:
                #get name and title
                names.append(_faculty_untitle(profile.find_all("div", {"class": "title"})[0].text.strip()))
                titles.append(profile.find_all("div", {"class": "position"})[0].text.strip())
                #go to personal page and find department if available
                profile.find_all("a", href=True)[0]["href"]
                personal_page_url = "https://www.aus.edu" + profile.find_all("a", href=True)[0]["href"]
                personal_page = requests.get(personal_page_url)
                personal_soup = BeautifulSoup(personal_page.content, "html.parser")
                class_department = "field field-name-field-department-ref field-type-entityreference field-label-hidden"
                pane_titles = personal_soup.find_all("h2", {"class": "pane-title"})
                #check if department affillation is available
                if "College / Department" in [p.text.strip() for p in pane_titles]:
                    try:
                        department = personal_soup.find_all("div", {"class": class_department})[0].text
                    except IndexError:
                        department = ""
                else:
                    department=""
                        
                departments.append(department)
        df = pd.DataFrame({
        "name": names,
        "title": titles,
        "department": departments
        })
        self.faculty_df = df
        return df

class AUSScraper(FacultyScholarScraper):

    def __init__(self):
        institute = "UAEU"
        super().__init__(institute)