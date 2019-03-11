import json
import sys
import os
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def print_bar(message, bar_dict):
    print('-' * 50)
    print(message)
    print(bar_dict['properties']['Attributes']['Name'])


def get_biggest_bar(bars_list):
    biggest_bar = max(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return smallest_bar


def get_closest_bar(bars_list, latitude, longitude):
    closest_bar = min(
        bars_list,
        key=lambda x: sqrt((latitude - x['geometry']['coordinates'][0]) ** 2 +
                           (longitude - x['geometry']['coordinates'][1]) ** 2))

    return closest_bar


if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else ''
    try:
        bars_list = load_data(filepath)['features']
    except FileNotFoundError:
        print('Файл не найден')
        sys.exit()
    except json.decoder.JSONDecodeError:
        print('Данные не в формате JSON')
        sys.exit()

    try:
        latitude = float(input('Введите широту Вашего местоположения:\n'))
        longitude = float(input('Введите долготу Вашего местоположения:\n'))
    except ValueError:
        print('Введено некорректное значение')

    print_bar('Самый большой бар:', get_biggest_bar(bars_list))
    print_bar('Самый маленький бар:', get_smallest_bar(bars_list))
    print_bar('Самый близкий бар:',
              get_closest_bar(bars_list, latitude, longitude))
