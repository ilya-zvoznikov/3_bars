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
Самый большой бар:
{
    "type": "Feature",
    "properties": {
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "VersionNumber": 2,
        "Attributes": {
            "global_id": 169375059,
            "Name": "Спорт бар «Красная машина»",
            "IsNetObject": "нет",
            "Address": "Автозаводская улица, дом 23, строение 1",
            "District": "Даниловский район",
            "SocialPrivileges": "нет",
            "OperatingCompany": null,
            "SeatsCount": 450,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "AdmArea": "Южный административный округ"
        },
        "ReleaseNumber": 2,
        "DatasetId": 1796
    },
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    }
}
--------------------------------------------------------------------------------
Самый маленький бар:
{
    "type": "Feature",
    "properties": {
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
        "VersionNumber": 2,
        "Attributes": {
            "global_id": 20675518,
            "Name": "БАР. СОКИ",
            "IsNetObject": "нет",
            "Address": "Дубравная улица, дом 34/29",
            "District": "район Митино",
            "SocialPrivileges": "нет",
            "OperatingCompany": null,
            "SeatsCount": 0,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "AdmArea": "Северо-Западный административный округ"
        },
        "ReleaseNumber": 2,
        "DatasetId": 1796
    },
    "geometry": {
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ],
        "type": "Point"
    }
}
--------------------------------------------------------------------------------
Введите широту Вашего месторасположения:
55.644079
Введите долготу Вашего месторасположения:
37.497403

Самый близкий бар:
{
    "type": "Feature",
    "properties": {
        "RowId": "af3820bd-14ca-4a68-870d-a3c743e28819",
        "VersionNumber": 2,
        "Attributes": {
            "global_id": 281494732,
            "Name": "Таверна",
            "IsNetObject": "нет",
            "Address": "проспект Защитников Москвы, дом 8",
            "District": "район Некрасовка",
            "SocialPrivileges": "нет",
            "OperatingCompany": null,
            "SeatsCount": 16,
            "PublicPhone": [
                {
                    "PublicPhone": "(977) 511-73-23"
                }
            ],
            "AdmArea": "Юго-Восточный административный округ"
        },
        "ReleaseNumber": 2,
        "DatasetId": 1796
    },
    "geometry": {
        "coordinates": [
            37.92096900029184,
            55.69988800002597
        ],
        "type": "Point"
    }
}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
