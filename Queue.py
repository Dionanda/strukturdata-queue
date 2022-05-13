# Nama : 
# NIM  : 
# Kelas: 

import queue

class Queue:
    def __init__(self):
        self.items = queue.Queue()
            
    # enQueue: untuk menambah data antrian
    def enQueue(self, data):
        self.items.put(data)
           
    # deQueue: untuk mengambil data antrian
    def deQueue(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "list empty"
   
    # untuk mencetak seluruh isi data antrian
    # def Print(self):
    #     print(self.items)
   
    #untuk mengetahui panjang stack
    # def Length(self):
    #     return len(self.items)
        
if __name__ == "__main__":
    q = Queue()
    q.enQueue(12)
    q.enQueue(45)
    q.enQueue(32)
    q.enQueue(56)
    print (q.deQueue())
    