import numpy as np
from scipy import linalg
import pickle
import time 

datasize = [20,40,50, 100, 200, 400, 600, 800, 1000, 1250, 1500, 1750, 2000]
sampling = 10 
timings = []
data_amount = []

for i in range(sampling):
    datasets = [np.random.randint(9,size=(i+1,i)) for i in datasize]
    for data in datasets:
        t = time.time()
        x = linalg.solve(data[:-1], data[-1])
        t = time.time() - t
        if np.allclose(np.dot(data[:-1],x),data[-1]):
            timings.append(t)
    data_amount.extend(datasize)

timedata = np.array(timings)
datadata = np.array(data_amount)
print(timedata.size)
print(datadata.size)
pickle.dump(data_amount, open('dataX.p', "wb"))
pickle.dump(timings, open('dataY.p', "wb"))

