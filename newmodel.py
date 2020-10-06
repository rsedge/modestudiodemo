import pandas as pd

def average(X):
    print("In average: ",type(X),X.shape,X.dtype.names)
    return X.mean(axis=1)

def bar(X):
    return None
