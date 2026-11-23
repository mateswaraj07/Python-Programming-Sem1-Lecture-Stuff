#simple thread program
from threading import Thread
def task():
    print("Thread is running")

t=Thread(target=task) #create thread
t.start() #start thread
t.join() #waiting for completion
print("Main program ends")