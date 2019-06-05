import threading
import time


# print(dir(threading.Thread))
class Mythread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print('{} Thread has started'.format(self.number))

        self.func(*self.args)

        print('{} Thread has finished'.format(self.number))

        # try:
        #     if self._target:
        #         self._target(*self._args, **self._kwargs)
        # finally:
        #     del self._target, self._args, self._kwargs
        #
        # print('{} has finished!'.format(self.getName()))


# def sleeper(n, name):
#     print('Hi Im {}. To be sleep'.format(name))
#     time.sleep(n)
#     print('{} not sleep'.format(name))

def double(number, cycles):
    for i in range(cycles):
        number += number
    print('Number == {}'.format(number))


# for i in range(4):
#     t = Mythread(target=sleeper,
#                  name=('Thread {}'.format(i + 1)),
#                  args=(3, 'Thread {}'.format(i + 1)))
#     t.start()


thread_list = []

for i in range(50):
    t = Mythread(number=i + 1, func=double, args=[i, 3])
    thread_list.append(t)
    t.start()
for i in thread_list:
    i.join()
