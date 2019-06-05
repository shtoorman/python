import threading
import time


class Mythread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(Mythread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print("thread started")
        super(Mythread, self).run(*args, **kwargs)
        print("thread finished")


def sleeper(num, style):
    print('sleepeng for {} sec style {}'.format(num, style))
    time.sleep(num)


t = Mythread(number=3, style="green", target=sleeper, args=[3, 'green'])

t.start()