from scholarly import scholarly

def find_faculty_scholar(faculty, institute):
    """find faculty scholar page given their name and institute

    Args:
        faculty (string): name of faculty
        institute (string): institute
    """
    g = scholarly.search_author(faculty + " khalifa university")
    g = list(g)
    if (len(g) > 1 or len(g) == 0):
        with open('KU.log', 'a') as f:
            f.writelines(f"{df['directory_name'][j]},{len(g)}\n")
    for i in g:
        details = scholarly.fill(i, sections=['basics', 'indices'])
        for key in keys:
            try:
                df[key].append(details[key])
            except KeyError:
                df[key].append('')

def _faculty_untitle(s):
    """Remove title from faculty name

    Args:
        s (string): faculty name

    Returns:
        string: faculty name without title
    """
    titles = ["Dr.", "Ms.", "Mr.", "Mrs."]
    split = s.split()
    if split[0] in titles:
        return " ".join(split[1:])
    else:
        return s

#HELLO GIT