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
Введите широту Вашего местоположения:
55.644079
Введите долготу Вашего местоположения:
37.497403
--------------------------------------------------
Самый большой бар:
Спорт бар «Красная машина»
--------------------------------------------------
Самый маленький бар:
БАР. СОКИ
--------------------------------------------------
Самый близкий бар:
Таверна
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
