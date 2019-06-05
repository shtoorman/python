import threading
import time


def sleeper(n, name):
    print('Hi {} im sleeping'.format(name))
    time.sleep(n)
    print('{} not sleep'.format(name))


t = threading.Thread(target=sleeper, name="Tread1", args=(5, "Tread1"))
t.start()
print("hello")
