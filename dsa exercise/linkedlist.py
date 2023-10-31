class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
head = None
def push(head_ref, new_data):
    new_Node = Node(new_data)
    new_Node.data = new_data
    new_Node.next = head_ref
    head_ref = new_Node
    head = head_ref
    return head
def sumOfLastN_NodesUtil(head, n):
    if (n <= 0):
        return 0
    sum = 0
    len = 0
    temp = head
    while (temp != None):
        len += 1
        temp = temp.next
    c = len - n
    temp = head
    while (temp != None and c > 0):
        temp = temp.next
        c -= 1
    while (temp != None):
        sum += temp.data
        temp = temp.next
    return sum
if __name__ == '__main__':
    head = push(head, 12)
    head = push(head, 4)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 10)
 
    n = 2
     
    print("Sum of last ", n, " Nodes = ", 
          sumOfLastN_NodesUtil(head, n))