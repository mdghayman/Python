import datetime
from pprint import pprint as pp


def current_year(self):
    now = datetime.datetime.now()
    return now.year


class Winery:

    def __init__(self, country, brand):

        self._country = country
        self._brand = brand

        types_made, vintages = self._brand.wine_list()
        self._type = [None] + [{letter: None for letter in vintages} for _ in types_made]

    def country(self):
        return self._country

    def brand(self):
        return self._brand()

    def _parse_wine(self, wine):
        wine_types, vintage_years = self._brand.wine_list()

        vintage = wine[-1]
        if vintage not in vintage_years:
            raise ValueError("Invalid vintage {}".format(vintage))

        return type, vintage

    def allocate_wine(self, wine_list, wine_name):
        types_made, vintage = self._parse_wine(wine_list)

        self._type[type][vintage] = wine_name

"""Add more text here (relocate passenger, etc)"""


class Brand:
    def __init__(self, name, region, date_est, types_made):
        self._name = name
        self._region = region
        self._date_est = date_est
        self._types_made = types_made

    def name(self):
        return self._name

    def country(self):
        return self._country

    def wine_list(self):
        return ((self._date_est, current_year), self._types_made)


def make_winery():
    w = Winery("South Africa", Brand("Steenberg", "Constantia", date_est=1682, types_made='Sauvignon Blanc' 'Chardonnay' 'Red Blend'))
    w.allocate_wine('2010 Sauvignon Blanc', 'Rattlesnake')
    w.allocate_wine('2010 Chardonnay', 'Sphinx')
    w.allocate_wine('2010 Red Blend', 'Catharina')
    return w
