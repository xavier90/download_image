from threading import Thread
import time
from multiprocessing import Process

p = Process()
p.is_alive()

def timer(name, delay, repeat):
    print "Timer: " + name + " started"
    while repeat > 0:
        time.sleep(delay)
        print name + ":" + str(time.ctime(time.time()))
        repeat -= 1
    print "Timer: " + name + "completed"

def Main():
    threads = []
    for i in range(5):
        t = Thread(target=timer, args=(str(i), 1, 5))
        t.start()
        threads.append(t)


    # alive = True
    # while alive:
    #     for t in threads:
    #         if not t.isAlive():
    #             alive = False
    #         else:
    #             alive = True
    #             break

    print "Main complete"





Main()
