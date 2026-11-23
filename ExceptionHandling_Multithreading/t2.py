# join function makes one thread wait until another thread finishes execution
from threading import Thread
from time import sleep
def task():
    for i in range(3):
        print(i)
        sleep(1)
t=Thread(target=task)
t.start()
t.join()
print("Main Thread Ends")