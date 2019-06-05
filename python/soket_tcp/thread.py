import getopt
import sys
import time

try:
    import thread as thr
except ImportError:
    import _thread as thr

debuglevel = 0
threadnum = 2
delay = 1
active = 0
numt = 0  # текущее число активных дочерних потоков
try:
    lock = thr.allocate_lock()  # блокировка доступа к числу активных дочерних потоков
    wait = thr.allocate_lock()  # блокировка ожидания завершения всех дочерних потоков

except AttributeError :
    print('e')

barier = {'numt': numt, 'lock': lock, 'wait': wait}

def delay_in_cycle(delay=1.0):
    t = time.time()
    while time.time() - t < delay:
        pass


def thrfun(delay, num, tstart):
    st = time.time() - tstart
    barier['numt'] = barier['numt'] + 1
    barier['lock'].release()
    ss = '\t{} : {} <= старт: {:14.11f}'.format(num, id, st)
    if not active:
        time.sleep(delay)  # пауза
    else:
        delay_in_cycle(delay)  # или активное ожидание
    barier['lock'].acquire()
    barier['numt'] = barier['numt'] - 1
    st = time.time() - tstart  # время завершения потока
    print('{} - финиш: {:14.11f}'.format(ss, st))
    if 0 == barier['numt']:
        barier['wait'].release()
    barier['lock'].release()
    return


opts, args = getopt.getopt(sys.argv[1:], "vt:d:a")
for opt, arg in opts:  # опции (ключи) командной строки (-v, -t, -d, -a)
    if opt[1:] == 'v': debuglevel = debuglevel + 1
    if opt[1:] == 't': threadnum = int(arg)
    if opt[1:] == 'd': delay = int(arg)
    if opt[1:] == 'a': active = 1
if debuglevel > 0:
    print(opts)
    print(args)
    print(debuglevel)
    print(threadnum)

barier['wait'].acquire()  # захват блокировки завершения
for n in range(threadnum):  # запуск threadnum потоков
    barier['lock'].acquire()
    id = thr.start_new_thread(thrfun, (delay, n, time.time()))
    print("\t{} : {} => запуск".format(n, id))
barier['wait'].acquire()  # ожидание завершения всех потоков
print('завершены все {} потоков \
        завершается ожидавший главный поток'.format(threadnum))