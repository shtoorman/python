#!/usr/bin/python
# -*- coding: utf-8 -*-

def show():
    msgt = '{}'.format(type(i))
    msgi = 'id={:09x}'.format(id(i))
    msgv = '{}'.format(str(i))
    try:
        msgh = 'hash={:012d}'.format(hash(i))
    except TypeError:
        msgh = 'не хэшируемый тип!'
    print(str(i) + ' - это : {:23} |{} |{} ==> {}'.format(msgt, msgi, msgh, msgv))
    print(' ')


i = 1;
show()
i = 1.5e-2;
show()
i = complex(3.0, 5.5);
show()
i = "теперь это UNICODE строка";
show()
i = [1, 2, 3];
show()
i = [3 * x for x in range(3)];
show()  # списковая сборка
i = [[x, x ** 2] for x in range(3)];
show()
i = (1, 2, 3);
show()
i = {1, 2, 3};
show()  # множество
i = {1: "one", 2: "two", 3: "three"};
show()  # словарь
i = lambda x: "фиктивная функция";
show()
i = compile('lambda x: "ещё одна фиктивная функция"', '', 'eval');
show()
i = iter('12345');
show()


class own1:
    def __init__(self, id):
        self.id = id


i = own1(987);
show()
i = own1;
show()


class own2:
    def __init__(self, id):
        self.id = id

    def __hash__(self):
        return None


i = own2(987);
show()
i = own2;
show()
