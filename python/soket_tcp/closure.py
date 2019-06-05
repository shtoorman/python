def multiplier(n):  # multiplier возвращает функцию умножения на n
    def mul(k):
        return n * k

    return mul


mul3 = multiplier(3)  # mul3 - функция, умножающая на 3
print(mul3(3), mul3(5))