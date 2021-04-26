import os
import pandas as pd
import matplotlib.pyplot as plt

PATH = os.path.join(os.getcwd(), 'dataset', 'gmc.csv')

dataset = pd.read_csv(PATH)

x = dataset.iloc[:,0]
y = dataset.iloc[:,1]

def Linear_regression(x,y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxy = sum(x*y)
    sx2 = sum(x*x)
    Ad = n*sx2 - (sx*sx)
    b1 = (n*sxy - sx*sy)/ Ad
    b0 = (sx2*sy - sxy*sx)/Ad
    return [(b1*x[i] + b0) for i in range(n)]

y_pred = Linear_regression(x,y)

plt.plot(x,y, 'ob',)
plt.plot(x,y_pred, '-r',)
plt.show()

