import json
import sys
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


function_dict_sorted_by = {
    'seatscount':
        (lambda x: x['properties']['Attributes']['SeatsCount']),
    'distance':
        (lambda x: sqrt((latitude - x['geometry']['coordinates'][0]) ** 2 +
                        (longitude - x['geometry']['coordinates'][1]) ** 2))}


def get_bars_sorted_by(input_file, sorted_by, reverse):
    bars_sorted_by = sorted(
        input_file['features'], key=sorted_by, reverse=reverse)

    return json.dumps(bars_sorted_by[0], indent=4, ensure_ascii=False)


def get_biggest_bar(input_file):
    return get_bars_sorted_by(input_file,
                              function_dict_sorted_by['seatscount'], True)


def get_smallest_bar(input_file):
    return get_bars_sorted_by(input_file,
                              function_dict_sorted_by['seatscount'], False)


def get_closest_bar(input_file, longitude, latitude):
    return get_bars_sorted_by(input_file,
                              function_dict_sorted_by['distance'], False)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'bars.json'

    bars_json_file = load_data(filepath)

    print('Самый большой бар:')
    print(get_biggest_bar(bars_json_file))
    print('-' * 80)

    print('Самый маленький бар:')
    print(get_smallest_bar(bars_json_file))
    print('-' * 80)

    while True:
        try:
            latitude = float(
                input('Введите широту Вашего месторасположения:\n'))
            longitude = float(
                input('Введите долготу Вашего месторасположения:\n'))
            break
        except ValueError:
            print('Введено некорректное значение! Попробуйте еще раз!')

    print()
    print('Самый близкий бар:')
    print(get_closest_bar(bars_json_file,
                          longitude=longitude,
                          latitude=latitude))
