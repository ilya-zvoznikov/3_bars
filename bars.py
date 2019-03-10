import json
import sys
import os
from math import sqrt


def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError
    with open(filepath, 'r') as file:
        return json.load(file)


def format_out(bar_dict):
    return bar_dict['properties']['Attributes']['Name']


def get_biggest_bar(bars_list):
    biggest_bar = max(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return format_out(biggest_bar)


def get_smallest_bar(bars_list):
    smallest_bar = min(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return format_out(smallest_bar)


def get_closest_bar(bars_list, longitude, latitude):
    closest_bar = min(
        bars_list,
        key=lambda x: sqrt((latitude - x['geometry']['coordinates'][0]) ** 2 +
                           (longitude - x['geometry']['coordinates'][1]) ** 2))

    return format_out(closest_bar)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1] if len(sys.argv) > 1 else ''
        bars_list = load_data(filepath)['features']

        print(type(bars_list))

        print('Самый большой бар:')
        print(get_biggest_bar(bars_list))
        print('-' * 50)

        print('Самый маленький бар:')
        print(get_smallest_bar(bars_list))
        print('-' * 50)

        latitude = float(input('Введите широту Вашего месторасположения:\n'))
        longitude = float(input('Введите долготу Вашего месторасположения:\n'))

        print()
        print('Самый близкий бар:')
        print(get_closest_bar(bars_list,
                              longitude=longitude,
                              latitude=latitude), '\n')
    except FileNotFoundError:
        print('Файл не найден')
    except ValueError:
        print('Введено некорректное значение')
