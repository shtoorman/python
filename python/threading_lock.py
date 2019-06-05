import threading
import time
import random

x = 0

lock = threading.Lock()

COUNT = 1000


def adding1():
    global x
    with lock:
        for i in range(COUNT):
            x += 2
            print(x)

def adding2():
    global x
    with lock:
        for i in range(COUNT):
            x += 2
            print(x)

def subtracting1():
    global x
    with lock:
        for i in range(COUNT):
            x -= 4
            print(x)

def subtracting2():
    global x
    with lock:
        for i in range(COUNT):
            x -= 7
            print(x)

#list_new = [adding1, adding2, subtracting1, subtracting2]
#print(list_new[random.randint(0, len(list_new))])
#print(list_new[i for i in random.randint(0, len(list_new))])
for i in range(10000):
    t1 = threading.Thread(target=adding1)
    t2 = threading.Thread(target=adding2)
    t3 = threading.Thread(target=subtracting1)
    t4 = threading.Thread(target=subtracting2)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    if x != 0:
        print(i, x)
        break
