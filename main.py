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

import sys, time

sys.setrecursionlimit(500000000)


class Object:
    def __init__(self, Country, Club_Name, City, Year, Coach_Name, Points):

        self.Country = Country
        self.Club_Name = Club_Name
        self.City = City
        self.Year = Year
        self.Coach_Name = Coach_Name
        self.Points = Points

    def __gt__(self, other):
        """operator > overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return False

    def __lt__(self, other):
        """operator < overloading"""

        return other > self

    def __ge__(self, other):
        """operator >= overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return True

    def __le__(self, other):
        """operator <= overloading"""

        return other >= self

    def __eq__(self, other):
        """operator == overloading"""
        #Country,Club_Name,City,Year,Coach_Name,Points
        return self.Year == other.Year and self.Country == other.Country and \
               self.Points == other.Points and self.Club_Name == other.Club_Name and \
               self.City == other.City and self.Coach_Name == other.Coach_Name


def cocktail_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while swapped:

        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if array[i] > array[i + 1]:
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # если не было обменов прерываем цикл
        if not swapped:
            break

        swapped = False

        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if array[i] > array[i + 1]:
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1


def quick_sort(array):
    """Выбирается опорный элемент - первый, берём все элементы меньшие - слева, больше - справа, рекурсивно повторяем пока длина не будет 0"""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)
    return array


def heapsort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


size = [100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

if __name__ == "__main__":
    times_cocktail_sort = []
    times_quick_sort = []
    times_heap_sort = []

    for i in range(len(size)):
        """Сортируем нагенеренное"""
        f = open("ds_" + str(size[i]) + ".csv", 'r')
        arr = []
        print("STARTING SIZE", size[i])
        for j in f.readlines():
            temp = j.split(",")
            arr.append(Object(temp[0], temp[1], temp[2], int(temp[3]), temp[4], int(temp[5])))
        f.close()

        temp2 = []
        t1 = time.time()
        temp2 = cocktail_sort(arr)
        times_cocktail_sort.append(time.time() - t1)

        temp2 = []
        t1 = time.time()
        temp2 = quick_sort(arr)
        times_quick_sort.append(time.time() - t1)

        temp2 = []
        t1 = time.time()
        temp2 = heapsort(arr)
        times_heap_sort.append(time.time() - t1)

        temp2 = []

        print(times_cocktail_sort, times_quick_sort, times_heap_sort)
