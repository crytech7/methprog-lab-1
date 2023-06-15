from matplotlib import pyplot


def main():
    """Генерируем графики"""

    size = 2500

    times_cocktail_sort = [0.0019338130950927734, 0.012921571731567383, 0.05393362045288086, 0.23413968086242676, 1.5660326480865479, 6.9869067668914795, 36.27107262611389]
    times_quick_sort    = [0.004717111587524414, 0.02626824378967285, 0.09865498542785645, 0.40264058113098145, 2.682711601257324, 12.448755741119385, 56.65288043022156]
    times_heap_sort     = [0.0007536411285400391, 0.002420663833618164, 0.00520634651184082, 0.012106180191040039, 0.03738880157470703, 0.08342456817626953, 0.1950974464416504]
    
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
