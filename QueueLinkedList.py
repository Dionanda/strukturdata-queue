# Nama : 
# NIM  : 
# Kelas: 

class Item:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
            
class Queue(object):
    def __init__(self, head=None, tail=None):
        self.head = head
    
    def enQueue(self, data):
        newItem = Item(data)
        if(self.head == None):
            newItem.next = None
            self.head = newItem
            self.tail = newItem
        else:
            newItem.next = None
            self.tail.next = newItem
            self.tail = newItem
    
    def deQueue(self):
        if(self.head == None):
            return None
        else:
            data = self.head.data
            curr = self.head.next
            self.head = None
            self.head = curr
            return data
            
        
    def Print(self):
        curr = self.head
        while (curr != None):
            print(curr.data)
            curr = curr.next
            
        
if __name__ == "__main__":
    q = Queue()
    
    q.enQueue(10)
    q.enQueue(32)
    q.enQueue(14)
    q.enQueue(56)

    q.Print()
    print("===========")
    print(q.deQueue())
    print("===========")
    q.Print()
    
