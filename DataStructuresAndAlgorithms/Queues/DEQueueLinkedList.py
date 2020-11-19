class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class DEQueueLinkedList:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def display(self):
        p = self._front
        while p:
            print(p._element,end='  ')
            p= p._next
        print()

    def search(self,key):
        p = self._front
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    def addfirst(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1
        return e

    def first(self):
        if self.isempty():
            print('DEQueue is empty')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print("DEQueue is empty")
            return
        return self._rear._element



L = DEQueueLinkedList()
L.addfirst(5)
L.addfirst(3)
L.addlast(7)
L.addlast(12)
L.display()
print('Length:',len(L))
L.removefirst()
L.display()
print('Length:',len(L))
L.removelast()
L.display()
print('Length:',len(L))
