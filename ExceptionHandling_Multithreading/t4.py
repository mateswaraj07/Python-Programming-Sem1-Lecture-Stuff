#Function calls using args
import threading
import time
def square(num):
    print("Square: ",num*num)
    time.sleep(1)
def cube(num):
    print("Cube: ", num*num*num)
    time.sleep(2)
t1=threading.Thread(target=square,args=(4,)) #If a func takes a parameter
t2=threading.Thread(target=cube,args=(4,))
t1.start()
t2.start()
#WAIT for completion
t1.join()
t2.join()
print("Done")