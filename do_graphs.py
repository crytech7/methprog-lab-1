from matplotlib import pyplot


def main():
    """Генерируем графики"""

    size = 2500

    times_cocktail_sort = [0.0010006427764892578, 0.00400090217590332, 0.020003080368041992, 0.0855402946472168, 0.5928921699523926]
    times_quick_sort    = [0.002000093460083008, 0.012003660202026367, 0.04300975799560547, 0.17643952369689941, 1.1417553424835205]
    times_heap_sort     = [0.0, 0.0010008811950683594, 0.0020003318786621094, 0.0050008296966552734, 0.014003753662109375]

    pyplot.plot(size, times_quick_sort, label="quick sort")
    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Время, секунды")
    pyplot.legend()
    pyplot.savefig("Quick sort")

    pyplot.plot(size, times_cocktail_sort, label="cocktail sort")
    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Время, секунды")
    pyplot.legend()
    pyplot.savefig("Cocktail sort")

    pyplot.plot(size, times_heap_sort, label="heap sort")
    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Время, секунды")
    pyplot.legend()
    pyplot.savefig("Heap sort")


if __name__ == "__main__":
    main()