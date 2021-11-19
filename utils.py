from scholarly import scholarly

def find_faculty_scholar(faculty):
    g = scholarly.search_author(faculty + " khalifa university")
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