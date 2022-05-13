# Nama : 
# NIM  : 
# Kelas: 

class Queue:
    def __init__(self):
        self.items = []
            
    # push: untuk menambah data antrian
    def enQueue(self, data):
        self.items.append(data)
           
    # pop: untuk mengambil data antrian
    def deQueue(self):
        if (len(self.items) != 0):
            return self.items.pop()
        else:
            return "list empty"
   
    #untuk mencetak seluruh data antrian
    def Print(self):
        print(self.items)
   
    #untuk mengetahui panjang antrian
    def Length(self):
        return len(self.items)
        
if __name__ == "__main__":
    q = Queue()
    q.enQueue(12)
    q.enQueue(32)
    q.enQueue(43)
    q.enQueue(83)
    
    q.Print()
    print(q.deQueue())
    print(q.Length())
