from scholarly import scholarly
import pandas as pd
from tqdm.auto import tqdm

faculty = pd.read_csv("data/KU/KU_faculty.csv")["name"]
keys = ["scholar_id", "name", "affiliation", "citedby", "hindex"]

df = {key: [] for key in keys}
df["directory_name"] = faculty

for j, f in enumerate(tqdm(faculty)):
    g = scholarly.search_author(f + " khalifa university")
    g = list(g)
    if (len(g) > 1 or len(g) == 0):
        with open('KU.log', 'a') as f:
            f.writelines(f"{df['directory_name'][j]},{len(g)}\n")
            continue
    for i in g:
        details = scholarly.fill(i, sections=['basics', 'indices'])
        for key in keys:
            try:
                df[key].append(details[key])
            except KeyError:
                df[key].append('')
    #print(df)


pd.DataFrame(df).to_csv("data/KU/scholar.csv")