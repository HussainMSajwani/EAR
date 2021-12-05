def faculty_untitle(s):
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