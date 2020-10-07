import numpy as np
import random
import pandas as pd

def predict(X):
    Y = np.empty((X.shape[0],1))
    rownum = 0
    for row in X:
        rowsum = 0
        for cell in row:
            if (isinstance(cell,int) or isinstance(cell,float)):
                # print(cell)
                rowsum = rowsum + cell*random.uniform(0,1)
            # else:
            #     # print("string:",cell)
        rowsum = rowsum + random.uniform(0,1)
        Y.itemset((rownum,0),rowsum)
        rownum = rownum + 1
    try:
        print(type(Y))
    except Exception as e:
        print(e)
    return pd.DataFrame(Y, columns=['pred_val'])
