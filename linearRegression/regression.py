import matplotlib.pyplot as plt
import numpy as np
import pickle


def compute_cost(X, Y, theta):
    m = Y.size
    x = np.dot(X, theta)
    J = np.dot((x-Y).T, (x-Y)) / (2*m)
    return J


def gradientDescent(X, y, theta, alpha, n):
    m = y.size
    J_history = np.zeros((n, 1))
    theta_history = np.zeros((n, 2))
    for i in range(n):

        theta = theta - (alpha/m)*(np.dot(X.T, np.dot(X, theta) - y))
        J_history[i] = compute_cost(X, y, theta)
        theta_history[i,:] = theta.T

    return [theta, J_history, theta_history]

def normalization(data):
    
    return data / np.max(data)

if __name__ == "__main__":
    # Load data from the files
    data_raw = pickle.load(open("dataX.p", "rb"))
    time_raw = pickle.load(open("dataY.p", "rb"))

    # Data normalization
    data = normalization(np.array(data_raw))
    time = normalization(np.array(time_raw))
    m = time.size

    time = time.reshape(m, 1)

    dataset = normalization(np.c_[np.ones((2000,1)), np.arange(1,2001)])
 
    plt.subplot(1,2,1)
    plt.plot(data, time, 'ro', label="Real data")
    data2 = np.c_[np.ones((m,1)), (data**2)*np.log2(data+2)] 
    dane = gradientDescent(data2, time, np.zeros((2,1)), 0.001, 2000)
    plt.plot(dataset, np.dot((dataset**2)*np.log2(dataset+2), dane[0]),label="n^2 * log(n)")
    print("O(n^2 log(n)):  ", dane[0][0], " + ", dane[0][1], "n^2 log(n)")

    data2 = np.c_[np.ones((m,1)), (data**2)] 
    dane = gradientDescent(data2, time, np.zeros((2,1)), 0.003, 1500)
    plt.plot(dataset, np.dot((dataset**2), dane[0]), 'k', label="n^2")
    print("O(n^2):  ", dane[0][0], " + ", dane[0][1], "n^2")

    data2 = np.c_[np.ones((m,1)), data**3] 
    dane = gradientDescent(data2, time, np.zeros((2,1)), 0.3, 2000)
    plt.plot(dataset, np.dot(dataset**3, dane[0]), label="n^3")
    print("O(n^3):  ", dane[0][0], " + ", dane[0][1], "n^3")
    plt.axis([0,0.5,0,0.05])
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(list(range(2000)), dane[1])

    plt.show()
