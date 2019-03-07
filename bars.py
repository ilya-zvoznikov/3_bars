import requests
from math import sqrt


def load_data(filepath='https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'):
    return requests.get(filepath).json()


def get_biggest_bar(data=load_data()):
    bars_seatscount_dict = {}
    for entry in data['features']:
        bars_seatscount_dict[
            entry['properties']['Attributes']['Name']] = entry['properties']['Attributes']['SeatsCount']
    max_seatscount = max(bars_seatscount_dict.values())
    biggest_bars_dict = {}
    for key in bars_seatscount_dict:
        if bars_seatscount_dict[key] == max_seatscount:
            biggest_bars_dict[key] = bars_seatscount_dict[key]
    return biggest_bars_dict.keys()


def get_smallest_bar(data=load_data()):
    bars_seatscount_dict = {}
    for entry in data['features']:
        bars_seatscount_dict[
            entry['properties']['Attributes']['Name']] = entry['properties']['Attributes']['SeatsCount']
    min_seatscount = min(bars_seatscount_dict.values())
    smallest_bars_dict = {}
    for key in bars_seatscount_dict:
        if bars_seatscount_dict[key] == min_seatscount:
            smallest_bars_dict[key] = bars_seatscount_dict[key]
    return smallest_bars_dict.keys()


def get_closest_bar(data=load_data(), longitude=0.0, latitude=0.0):
    bars_distance_dict = {}
    for entry in data['features']:
        bars_distance_dict[entry['properties']['Attributes']['Name']] = sqrt(
            (latitude - entry['geometry']['coordinates'][0]) ** 2 + (longitude - entry['geometry']['coordinates'][1]) ** 2)
    min_distance = min(bars_distance_dict.values())
    closest_bars_dict = {}
    for key in bars_distance_dict:
        if bars_distance_dict[key] == min_distance:
            closest_bars_dict[key] = bars_distance_dict[key]
    return closest_bars_dict.keys()


if __name__ == '__main__':
    print('Список самых больших баров:')
    print(*get_biggest_bar(), sep=', ', end='\n')
    print()
    print('Список самых маленьких баров:')
    print(*get_smallest_bar(), sep=', ', end='\n')
    print()
    latitude = float(input('Введите широту Вашего месторасположения:\n'))
    longitude = float(input('Введите долготу Вашего месторасположения:\n'))
    print()
    print('Список ближайших баров:')
    print(*get_closest_bar(longitude=longitude, latitude=latitude), sep=', ', end='\n')
