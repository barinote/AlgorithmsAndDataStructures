from unorderedlist import UnorderedList

class Deque(UnorderedList):
    def addFront(self, item):
        self.add(item)

    def addRear(self, item):
        self.append(item)

    def removeFront(self):
        return self.pop()
    
    def insert(self, index, value):
        pass

    def removeRear(self):
        return self.pop(self.size()-1)
