# Ближайшие бары

Скрипт сканирует список московских баров с сайта [data.mos.ru](https://data.mos.ru/) и находит самые большие и самые маленькие из них (по количеству посадочных мест), а также самые близкие по отношению к текущему месторасположению (координаты вводятся вручную с клавиатуры)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

На сайте [data.mos.ru](https://data.mos.ru/) есть много разных данных, в том числе список московских баров.
Его можно скачать в формате JSON. Для этого нужно:

* зарегистрироваться на сайте и получить ключ API;
* скачать файл по ссылке вида
<https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}>.

Путь к скачанному файлу в формате JSON указывается при запуске сразу после имени скрипта.

Запуск на Linux:

```bash

$ python bars.py bars.json  # possibly requires call of python3 executive instead of just python
Самые большие бары:
[
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Южный административный округ",
                "global_id": 169375059,
                "SeatsCount": 450,
                "Address": "Автозаводская улица, дом 23, строение 1",
                "District": "Даниловский район",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "(905) 795-15-84"
                    }
                ],
                "Name": "Спорт бар «Красная машина»",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.638228501070095,
                55.70111462948684
            ]
        },
        "type": "Feature"
    }
]
--------------------------------------------------------------------------------
Самые маленькие бары:
[
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Северо-Западный административный округ",
                "global_id": 20675518,
                "SeatsCount": 0,
                "Address": "Дубравная улица, дом 34/29",
                "District": "район Митино",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "(495) 258-94-19"
                    }
                ],
                "Name": "БАР. СОКИ",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.35805920566864,
                55.84614475898795
            ]
        },
        "type": "Feature"
    },
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "57d2a5ce-55ec-47b2-bd04-002631c6eded",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Северо-Западный административный округ",
                "global_id": 20684125,
                "SeatsCount": 0,
                "Address": "Пятницкое шоссе, дом 18",
                "District": "район Митино",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "(495) 794-45-50"
                    }
                ],
                "Name": "Соки",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.38364199965832,
                55.84432399993839
            ]
        },
        "type": "Feature"
    },
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "9663189a-8d47-45c0-a879-eed16996fda2",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Северо-Западный административный округ",
                "global_id": 20711360,
                "SeatsCount": 0,
                "Address": "Пятницкое шоссе, дом 18",
                "District": "район Митино",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "(495) 794-45-50"
                    }
                ],
                "Name": "Фреш-бар",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.38364199965832,
                55.84432399993839
            ]
        },
        "type": "Feature"
    },
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "a3156c38-2b15-4088-98c7-d9ce24075827",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Северо-Восточный административный округ",
                "global_id": 272459485,
                "SeatsCount": 0,
                "Address": "проезд Дежнёва, дом 1",
                "District": "район Южное Медведково",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "нет телефона"
                    }
                ],
                "Name": "Бар в Деловом центре Яуза",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.649759000274265,
                55.871183000126486
            ]
        },
        "type": "Feature"
    }
]
--------------------------------------------------------------------------------
Введите широту Вашего месторасположения:
55.644079
Введите долготу Вашего месторасположения:
37.497403

Самые близкие бары:
[
    {
        "properties": {
            "DatasetId": 1796,
            "RowId": "af3820bd-14ca-4a68-870d-a3c743e28819",
            "ReleaseNumber": 2,
            "VersionNumber": 2,
            "Attributes": {
                "AdmArea": "Юго-Восточный административный округ",
                "global_id": 281494732,
                "SeatsCount": 16,
                "Address": "проспект Защитников Москвы, дом 8",
                "District": "район Некрасовка",
                "IsNetObject": "нет",
                "SocialPrivileges": "нет",
                "PublicPhone": [
                    {
                        "PublicPhone": "(977) 511-73-23"
                    }
                ],
                "Name": "Таверна",
                "OperatingCompany": null
            }
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                37.92096900029184,
                55.69988800002597
            ]
        },
        "type": "Feature"
    }
]

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
