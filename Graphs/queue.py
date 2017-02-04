class Queue:
    def __init__(self, *args, **kwargs):
        self.l = list(args)

    def dequeue(self):
        return self.l.pop()

    def enqueue(self, item):
        self.l.append(item)

    def isEmpty(self):
        return not bool(self.l)

    def size(self):
        return len(self.l)