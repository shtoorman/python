import threading

res_A = threading.Lock()
res_B = threading.Lock()

def proc1():
   res_A.acquire()
   res_B.acquire()
   # ...
   res_B.release()
   res_A.release()

def proc2():
   res_A.acquire()
   res_B.acquire()
   # ...
   res_B.release()
   res_A.release()

p1 = threading.Thread(target=proc1, name="t1")
p2 = threading.Thread(target=proc2, name="t2")
p1.start()
p2.start()
p1.join()
p2.join()