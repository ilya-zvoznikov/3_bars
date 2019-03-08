import json
import sys
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def get_bars_sorted_by(input_file, sorted_by, reverse):
    bars_sorted_by = sorted(input_file['features'], key=sorted_by, reverse=reverse)

    bars_count = 1
    seatscount = bars_sorted_by[0]['properties']['Attributes']['SeatsCount']
    while True:
        if bars_sorted_by[bars_count]['properties']['Attributes']['SeatsCount'] == seatscount:
            bars_count += 1
        else:
            break
    return json.dumps(bars_sorted_by[0:bars_count], indent=4, ensure_ascii=False)


def get_biggest_bar(input_file):
    return get_bars_sorted_by(input_file, (lambda x: x['properties']['Attributes']['SeatsCount']), True)


def get_smallest_bar(input_file):
    return get_bars_sorted_by(input_file, (lambda x: x['properties']['Attributes']['SeatsCount']), False)


def get_closest_bar(input_file, longitude=0.0, latitude=0.0):
    bars_sorted_by_distance = sorted(input_file['features'],
                                     key=lambda x: sqrt((latitude - x['geometry']['coordinates'][0]) ** 2 +
                                                        (longitude - x['geometry']['coordinates'][1]) ** 2),
                                     reverse=False)
    bars_count = 1
    distance = sqrt((latitude - bars_sorted_by_distance[0]['geometry']['coordinates'][0]) ** 2 +
                    (longitude - bars_sorted_by_distance[0]['geometry']['coordinates'][1]) ** 2)
    while True:
        if sqrt((latitude - bars_sorted_by_distance[bars_count]['geometry']['coordinates'][0]) ** 2 +
                (longitude - bars_sorted_by_distance[bars_count]['geometry']['coordinates'][1]) ** 2) == distance:
            bars_count += 1
        else:
            break
    return json.dumps(bars_sorted_by_distance[0:bars_count], indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'bars.json'

    bars_json_file = load_data(filepath)

    print('Самые большие бары:')
    print(get_biggest_bar(bars_json_file))
    print('-'*80)
    print('Самые маленькие бары:')
    print(get_smallest_bar(bars_json_file))
    print('-'*80)

    while True:
        try:
            latitude = float(input('Введите широту Вашего месторасположения:\n'))
            break
        except ValueError:
            print('Введено некорректное значение! Попробуйте еще раз!')
    while True:
        try:
            longitude = float(input('Введите долготу Вашего месторасположения:\n'))
            break
        except ValueError:
            print('Введено некорректное значение! Попробуйте еще раз!')

    print()
    print('Самые близкие бары:')
    print(get_closest_bar(bars_json_file, longitude=longitude, latitude=latitude))
