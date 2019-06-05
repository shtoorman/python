# -*- coding: utf-8 -*-
import sys


def show(fun, arg):
    print('{} : {}'.format(type(fun), fun))
    print('arg={} => fun( arg )={}'.format(arg, fun(arg)))


if len(sys.argv) > 1:
    n = float(sys.argv[1])
else:
    n = float(input("число?: "))


def pow3(n):  # 1-е определение функции
    return n * n * n


show(pow3, n)

pow3 = lambda n: n * n * n  # 2-е определение функции с тем же именем
show(pow3, n)

show((lambda n: n * n * n), n)  # 3-е, использование анонимного описание функции
