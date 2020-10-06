import pandas as pd
import numpy as np
import random

def average(X):
    print("In average: ",type(X),X.shape,X.dtype.names)
    return X.mean(axis=1)

def bar(X):
    return None

def predict(X):
    Y = np.empty((X.shape[0],1))
    rownum = 0
    for row in X:
        rowsum = 0
        for cell in row:
            rowsum = rowsum + cell*random.uniform(0,1)
        rowsum = rowsum + random.uniform(0,1)
        Y.itemset((rownum,0),rowsum)
        rownum = rownum + 1
    return Y



