#active_count()
'''
import time
import threading

def thread1(i):
    time.sleep(3)

def thread2(i):
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=(10,))
    t2 = threading.Thread(target=thread2, args=(12,))
    t1.start()
    t2.start()
    print("No. of active threads: " , threading.active_count())
    t1.join()
    t2.join()
'''
#current thread
'''
import time
import threading

def thread1(i):
    time.sleep(3)

def thread2(i):
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=(10,))
    t2 = threading.Thread(target=thread2, args=(12,))
    t1.start()
    t2.start()
    print("Current thread is: " , threading.current_thread())
    t1.join()
    t2.join()
'''
#threading_ident() returns thread identifier of the current thread.
#threading.enumerate() returns a list of all thread objects currently alive.
#threading.main_thread() returns main thread object.
#threading.settrace(fun) is used to trace function for all the threads started using the threading module.
'''
import threading
def hello(frame, event, arg):
    print("Hello, I am a trace hook.")
threading.settrace(hello)

'''
#threading.setprofile(fun) is used to set a profile function for all threads started from the threading module. 
#threading.stack_size([size]) returns the thread stack size utilised when creating new threads.
#threading.TIMEOUT_MAX 
'''
Object	Description
Thread	            Object that represents a single thread of execution.
Lock	            Primitive lock object.
RLock	            RLock or Re-entrant lock object provides ability for a single thread to (re)acquire an already-held lock (recursive locking).
Condition	        Condition variable object causes one thread to wait until certain "condition" has been satisfied by another thread (such as change in state or some data value)
Event	            Its a more general version of condition variables, whereby a number of threads can be made to wait for some event to occur and all the threads waiting will only awaken when the event happens.
Semaphore	        Provides a "counter" of finite resources shared between threads block when none are available.
BoundedSemaphore    Similar to a Semaphore but ensures that it never exceeds its initial value.
Timer	            Similar to Thread, except that it waits for a specified period of time before running.
Barrier	            Creates a "barrier" at which a specified number of threads must all arrive before they're all allowed to continue.
'''