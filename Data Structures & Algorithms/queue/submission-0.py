class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
     
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 


    def isEmpty(self) -> bool:

        return self.size  == 0
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        if  self.tail ==  None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node

            new_node.prev = self.tail

            self.tail = new_node
        self.size += 1

        


        

    def appendleft(self, value: int) -> None:
        new_node  = Node(value)
        if self.head == None:
            self.head = self.tail =  new_node
        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
            
        

    def pop(self) -> int:
        if(self.isEmpty()):
            return -1
        
        pop_el =  self.tail

        if  self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

        return pop_el.value

        

    def popleft(self) -> int:

        if self.isEmpty():
            return -1
        pop_el = self.head

        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

        return pop_el.value
        
