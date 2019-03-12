import json
import sys
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
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        sys.exit('Не указан путь к файлу')

    try:
        bars_list = load_data(filepath)['features']
        latitude = float(input('Введите широту Вашего местоположения:\n'))
        longitude = float(input('Введите долготу Вашего местоположения:\n'))
    except json.decoder.JSONDecodeError:
        sys.exit('Данные не в формате JSON')
    except ValueError:
        sys.exit('Введено некорректное значение')
    except FileNotFoundError:
        sys.exit('Файл не найден')

    print_bar('Самый большой бар:', get_biggest_bar(bars_list))
    print_bar('Самый маленький бар:', get_smallest_bar(bars_list))
    print_bar('Самый близкий бар:',
              get_closest_bar(bars_list, latitude, longitude))
