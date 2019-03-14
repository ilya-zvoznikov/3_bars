import json
import sys
from math import sqrt


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


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
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        sys.exit('Не указан путь к файлу')

    loaded_content = load_data(filepath)

    if not loaded_content:
        sys.exit('Файл не найден или данные не в формате JSON')
    else:
        bars_list = loaded_content['features']

    try:
        latitude = float(input('Введите широту Вашего местоположения:\n'))
        longitude = float(input('Введите долготу Вашего местоположения:\n'))
    except ValueError:
        sys.exit('Введено некорректное значение')

    print_bar('Самый большой бар:', get_biggest_bar(loaded_content))
    print_bar('Самый маленький бар:', get_smallest_bar(loaded_content))
    print_bar('Самый близкий бар:',
              get_closest_bar(loaded_content, latitude, longitude))
