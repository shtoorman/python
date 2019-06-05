import threading
import time

total = 4


def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('iteration {} total == {}'.format(i, total))
        total += 1
    print('iteration done')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(2)
        print('iteration {} total == {}'.format(i, total))
        total += 1
    print('iteration done')


def limits_items():
    global total
    while True:
        if total > 5:
            print('overloaded')
            total -= 3
            print('subtracted by 3, total == {}'.format(total))
        else:
            time.sleep(1)
            print('waiting')


creates1 = threading.Thread(target=creates_items)
creates2 = threading.Thread(target=creates_items_2)
limiter = threading.Thread(target=limits_items, daemon=True)

creates1.start()
creates2.start()
limiter.start()

creates1.join()
creates2.join()
#limiter.join()

print("Finish with total {}".format(total))
