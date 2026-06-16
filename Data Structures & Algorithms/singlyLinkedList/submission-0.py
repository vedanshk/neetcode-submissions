class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index < 0  or index >= self.size:
            return False
        current = self.head

        if index == 0:
            self.head = current.next
            self.size -= 1
            return True

        prev = None
        for _ in range(index):
            prev= current
            current = current.next
        prev.next = current.next 

        if current ==  self.tail:
            self.tail = prev  

        self.size -= 1
        return True 

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head
        while curr:
            ans.append(curr.value)
            curr = curr.next

        return ans
        
