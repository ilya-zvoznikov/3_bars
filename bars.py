import requests
from math import sqrt


def load_data(filepath='https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'):
    return requests.get(filepath).json()


def get_biggest_bar(data=load_data()):
    dict_of_seatscount = {}
    for feature in data['features']:
        dict_of_seatscount[
            feature['properties']['Attributes']['Name']] = feature['properties']['Attributes']['SeatsCount']
    biggest_seatscount = max(dict_of_seatscount.values())
    biggest_bars = {}
    for key in dict_of_seatscount:
        if dict_of_seatscount[key] == biggest_seatscount:
            biggest_bars[key] = dict_of_seatscount[key]
    return biggest_bars.keys()


def get_smallest_bar(data=load_data()):
    dict_of_seatscount = {}
    for feature in data['features']:
        dict_of_seatscount[
            feature['properties']['Attributes']['Name']] = feature['properties']['Attributes']['SeatsCount']
    smallest_seatscount = min(dict_of_seatscount.values())
    smallest_bars = {}
    for key in dict_of_seatscount:
        if dict_of_seatscount[key] == smallest_seatscount:
            smallest_bars[key] = dict_of_seatscount[key]
    return smallest_bars.keys()


def get_closest_bar(data=load_data(), longitude=0, latitude=0):
    dict_of_distance = {}
    for geo in data['features']:
        dict_of_distance[geo['properties']['Attributes']['Name']] = sqrt(
            (latitude - geo['geometry']['coordinates'][0]) ** 2 + (longitude - geo['geometry']['coordinates'][1]) ** 2)
    min_distance = min(dict_of_distance.values())
    closest_bars = {}
    for key in dict_of_distance:
        if dict_of_distance[key] == min_distance:
            closest_bars[key] = dict_of_distance[key]
    return closest_bars.keys()


if __name__ == '__main__':
    print('List of biggest bars:')
    print(*get_biggest_bar(), sep=', ', end='\n')
    print()
    print('List of smallest bars:')
    print(*get_smallest_bar(), sep=', ', end='\n')
    print()
    longitude = float(input('Enter current longitude:\n'))
    latitude = float(input('Enter current latitude:\n'))
    print()
    print('List of closest bars:')
    print(*get_closest_bar(longitude=longitude, latitude=latitude), sep=', ', end='\n')
