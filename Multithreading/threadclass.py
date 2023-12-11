'''
In the threading module the most popular and the most used call is the Thread class, which is primarily used to create and run threads. Thread class provides all the major functionalities required to create and manage a thread.

Thread objects are the objects of the Thread class where each object represents an activity to be performed in a separate thread of control.
'''
import threading
import time

class MyThread(threading.Thread):
  # overriding constructor
  def __init__(self, i):
    # calling parent class constructor
    threading.Thread.__init__(self)
    self.x = i
    
  # define your own run method
  def run(self):
    print("Value stored is: ", self.x)
    time.sleep(3)
    print("Exiting thread with value: ", self.x)
    

thread1 = MyThread(1)
thread1.start()
thread2 = MyThread(2)
thread2.start()