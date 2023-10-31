MAX = 100 
class Deque:
    def __init__(self, size):
        self.arr = [0] * MAX
        self.front = -1
        self.rear = 0
        self.size = size
    def isFull(self):
        return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)
    def isEmpty(self):
        return (self.front == -1)
    def insertfront(self, key):
        if (self.isFull()):
            print("Overflow")
            return
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.front == 0):
            self.front = self.size - 1
        else: 
            self.front = self.front-1
        self.arr[self.front] = key
    def insertrear(self, key):
        if (self.isFull()):
            print(" Overflow")
            return
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.rear == self.size-1):
            self.rear = 0
        else:
            self.rear = self.rear+1
        self.arr[self.rear] = key
    def deletefront(self):
        if (self.isEmpty()):
            print("Queue Underflow")
            return
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.front == self.size - 1):
                self.front = 0
            else:
                self.front = self.front+1
    def deleterear(self):
        if (self.isEmpty()):
            print(" Underflow")
            return
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
 
        elif (self.rear == 0):
            self.rear = self.size-1
        else:
            self.rear = self.rear-1
    def getFront(self):
        if (self.isEmpty()):
            print(" Underflow")
            return -1
        return self.arr[self.front]
    def getRear(self):
        if(self.isEmpty() or self.rear < 0):
            print(" Underflow")
            return -1
        return self.arr[self.rear]
if __name__ == "__main__":
  dq = Deque(5)
  print("Insert element at rear end  : 5 ")
  dq.insertrear(5)
  print("insert element at rear end : 10 ")
  dq.insertrear(10)
  print(f"get rear element : {dq.getRear()}")
  dq.deleterear()
  print(f"After delete rear element new rear become : {dq.getRear()}")
  print("inserting element at front end")
  dq.insertfront(15)
  print(f"get front element: {dq.getFront()}")
  dq.deletefront()
  print(f"After delete front element new front become : {dq.getFront()}")
 