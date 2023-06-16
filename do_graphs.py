from matplotlib import pyplot


def main():
    """Генерируем графики"""

    size = [100, 250, 500, 1000, 2500, 5000, 10000, 25000]

    times_cocktail_sort = [0.000446319580078125, 0.002875804901123047, 0.012158632278442383, 0.051683664321899414, 0.3517327308654785, 1.4978055953979492, 6.695376873016357, 50.84393787384033]
    times_quick_sort    = [0.0016469955444335938, 0.011657476425170898, 0.05052375793457031, 0.2041475772857666, 1.3362524509429932, 5.474143028259277, 23.564149141311646, 644.367066860199]
    times_heap_sort     = [0.00017023086547851562, 0.0005037784576416016, 0.0011675357818603516, 0.002708911895751953, 0.008693695068359375, 0.018074512481689453, 0.04243612289428711, 0.1197361946105957]
    
    pyplot.plot(size, times_quick_sort, label="quick sort")
    pyplot.plot(size, times_cocktail_sort, label="cocktail sort")
    pyplot.plot(size, times_heap_sort, label="heap sort")
    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Время, секунды")
    pyplot.legend()
    pyplot.savefig("Sorting Algorithms")


if __name__ == "__main__":
    main()
