# methprog-lab-1
```
  #  =====================================================================================================
  # 	 ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #   ／|、         ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  # （ﾟ､ ｡ つ               ﾞ☆ﾞ             ﾞ☆ﾞ               ﾞ☆ﾞ            ﾞ☆ﾞ              ﾞ☆ﾞ              ﾞ☆ﾞ
  #  |、ﾞ  ヽ        ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  じーし__ )つ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  =====================================================================================================
  #  МЕТОДЫ ПРОГРАММИРОВАНИЯ | LAB 1 10.03.2023 | ВАРИАНТ 12
  #  by crytech7
  #  =====================================================================================================
  #  > ВАРИАНТ 12:
  # 	Массив данных о командах, принимающих участие в  чемпионате страны по футболу:
  # 	страна, название клуба,  город, год, ФИО главного тренера
  # 	(сравнение по полям – год, страна, количество набранных очков (по убыванию), название клуба):

  #       Country,Club Name,City,Year,Coach Name,Points

  #  > СОРТИРОВКИ:
  # 	г) Шейкер-сортировка
  # 	д) Пирамидальная сортировка
  # 	е) Быстрая сортировка
  #  ====================================================================================================
```
1) Реализовать сортировки для массива объектов в  соответствии с вариантом. 
2) Перегрузить операторы сравнения (>, <, >=, <=) для сравнения  объектов. 
3) Входные данные для сортировки массива обязательно считывать из  внешних источников: текстовый файл, файл MS Excel, MS Access,  данные из СУБД (любое на выбор). Выходные данные (отсортированный массив) записывать в файл.
4) Выбрать 7-10 наборов данных для сортировки размерности от 100 и  более. Засечь (программно) время сортировки  каждым алгоритмом. По полученным точкам построить графики  зависимости времени сортировки от размерности массива для каждого  из алгоритмов сортировки на одной оси координат. Сделать вывод о  том, в каком случае, какой из методов лучше применять. Графики  можно строить программно или в любой из прикладных программ  (MS Excel, Matlab, MathCad и т.д.).

## Visual

![Alt text](https://github.com/crytech7/methprog-lab-1/blob/main/Sorting%20Algorithms.png "Optional title")

## Usage
```
  git clone https://github.com/crytech7/methprog-lab-1
  cd methprog-lab-1
  python3 generate.py
  python3 main.py
  python3 do_graphs.py
```
## Note
HTML Report was generated using pdoc. Index page was manually edited to place images and links
```
  pip3 install pdoc3
  pdoc --html .
```
