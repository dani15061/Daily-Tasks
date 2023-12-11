'''
import threading

lock = threading.Lock()

print("Acquiring the lock: ", lock.acquire())
# adding 0 as timeout value else, the below statement will wait forever
print("Acquiring the lock again: ", lock.acquire(0))
'''
import threading

lock = threading.RLock()

print("Acquiring the lock: ", lock.acquire())
# adding 0 as timeout value else, the below statement will wait forever
print("Acquiring the lock again: ", lock.acquire())