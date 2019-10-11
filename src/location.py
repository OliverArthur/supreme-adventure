def announce_location(country):
    print(country)
    return country


instructor_location = announce_location('Canada')

print(instructor_location)




def get_capital(country):
    """(str) -> str
    >>> get_capital('Canada')
    Canada
    """
    return country



def longer(country1, country2):
    """(str, str) -> str
    >>> longer(country1, country2)
    Italy, Dominican Republic
    """
    return country1 + country2