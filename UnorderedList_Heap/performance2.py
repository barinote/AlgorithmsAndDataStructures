from unorderedlist import UnorderedList
import time

myList = UnorderedList()
pyList = list()

size = 2000
amount = 3

print("-----------------------------------------------------------------")
print("           PERFORMANCE TEST UnorderedList vs PythonList          ")
print("-----------------------------------------------------------------")

mySave = 0
myClear = 0
for i in range(amount):

    t = time.time()
    for x in range(size):
        myList.append(x)
    mySave += time.time() - t

    t = time.time()
    for x in range(size):
        myList.pop()
    myClear += time.time() - t

pySave = 0
pyClear = 0
for i in range(amount):

    t = time.time()
    for x in range(size):
        pyList.append(x)
    pySave += time.time() - t

    t = time.time()
    for x in range(size):
        pyList.pop()
    pyClear += time.time() - t

print("Adding(rear):\t myLIST {}\t| pyLIST {}".format(mySave, pySave))
print("Reading:     \t myLIST {}\t| pyLIST {}".format(myClear, pyClear))

mySave = 0
pySave = 0
# Adding elements to the front of list performance
for i in range(amount):
    myList = UnorderedList()

    t = time.time()
    for x in range(size):
        myList.add(x)
    mySave += time.time() - t

    pyList = list()

    t = time.time()
    for x in range(size):
        pyList.insert(0, x)
    pySave += time.time() - t

print("Adding(front):\t myLIST {}\t| pyLIST {}".format(mySave, pySave))

myList = UnorderedList()
pyList = list()
for x in range(size):
    myList.add(x)
    pyList.insert(0, x)

myTime = 0
pyTime = 0
# Getting element by index performance
for i in range(amount):

    t = time.time()
    for x in (0, size//4, size//2, size-1):
        myList.index(x)
    myTime += time.time() - t

    t = time.time()
    for x in (0, size//4, size//2, size-1):
        pyList.index(x)
    pyTime += time.time() - t

print("Getting index:\t myLIST {}\t| pyLIST {}".format(myTime, pyTime))

myTime = 0
pyTime = 0
# Getting size of the list performance
for i in range(amount):

    t = time.time()
    myList.size()
    myTime += time.time() - t

    t = time.time()
    len(pyList) 
    pyTime += time.time() - t
 
print("Getting size:\t myLIST {}\t| pyLIST {}".format(myTime, pyTime))
