def get_country_info(city, country, population=''):
    """Generate a formatted string for a country and city"""
    if population:
        country_info = f"{city}, {country} - Population={population}"
    else:
        country_info = f"{city}, {country}"
    return country_info.title()