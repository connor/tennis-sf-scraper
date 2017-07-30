import pprint
from pyquery import PyQuery as pq
from urlparse import urlparse, parse_qs

def _elements_contains_text(elements, text):
    contained = False
    for element in elements:
        if text in element.text_content():
            contained = True
    return contained

def format_address(elements):
    return elements[0].text_content()

def format_name(elements):
    name = elements[0].text_content().strip()
    return name.split('SF - ')[1]

def format_lat_lng(elements):
    maps_url = elements[0].attrib['href']
    params = parse_qs(urlparse(maps_url).query, keep_blank_values=True)
    geo_params = params['geocode'][0].split(',')
    return {
        'lat': geo_params[0],
        'lng': geo_params[1]
    }

def format_court_count(elements):
    formatted_court_count = 0;
    court_count = elements[0].text_content().strip().split(' Courts')[0]
    if court_count != '':
        formatted_court_count = int(court_count)
    return formatted_court_count

def format_has_lights(elements):
    lighted = False
    return _elements_contains_text(elements, 'Lighted')

def format_has_wall(elements):
    return _elements_contains_text(elements, 'Wall')

def format_has_fee(elements):
    return _elements_contains_text(elements, 'Fee')

def format_is_tennis_club(elements):
    return _elements_contains_text(elements, 'Tennis Club')

def format_is_restricted(elements):
    return _elements_contains_text(elements, 'Restricted')

def generate_court_from_html(court_html):
    court_attributes = [
        ('address', 'p > a', format_address),
        ('geo', 'p > a', format_lat_lng),
        ('name', '.location-name > a', format_name),
        ('courts', '.location-matches > li', format_court_count),
        ('has_lights', '.location-matches li', format_has_lights),
        ('has_wall', '.location-matches li', format_has_wall),
        ('has_fee', '.location-matches li', format_has_fee),
        ('is_tennis_club', '.location-matches li', format_is_tennis_club),
        ('is_restricted', '.location-matches li', format_is_restricted),
    ]
    court = {}
    for attributes in court_attributes:
        key = attributes[0]
        selector = attributes[1]
        html = court_html.cssselect(selector)
        fn = attributes[2]
        court[key] = fn(html)
    return court

def scrape():
    url = "https://www.tennissf.com/SF-Tennis-Courts?id=54" # "San Francisco - North" on tennissf.com
    parsed_html = pq(url)
    courts_html = parsed_html('.location-list > li')
    courts = []
    for court_html in courts_html:
        courts.append(generate_court_from_html(court_html))

    return courts


if __name__ == '__main__':
    courts = scrape()
    pprint.pprint(courts)
