class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        temp = Node(item)
        if current == None:
            self.head = temp
            return 
        while current != None:
             previous = current
             current = current.getNext()
        previous.setNext(temp)

    def index(self, item):
        current = self.head
        index = -1
        while current != None:
            index = index + 1
            if current.getData() == item:
                return index
            else:
                current = current.getNext()
        return index

    def insert(self, pos, item):
        if self.size() < pos + 1:
            raise IndexError

        temp = Node(item)
        current = self.head
        previous = None
        current_position = 0
        while current_position != pos and current != None:
            previous = current
            current = current.getNext()
            current_position = current_position + 1
        temp.setNext(current)
        if pos == 0:
            self.head = temp
        elif previous != None:
            previous.setNext(temp)
        

    def pop(self, pos=0):
        current_pos = 0
        current = self.head
        previous = None

        while current_pos != pos:
            previous = current
            current = current.getNext()
            current_pos = current_pos + 1
        
        temp = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return temp
                

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
