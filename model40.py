import pandas as pd
import numpy as np
import random

def m40(X):
    Y = np.empty((X.shape[0],1))
    rownum = 0
    for row in X:
        rowsum = 0
        cellnum = 1
        for cell in row:
            if (isinstance(cell,int) or isinstance(cell,float)):
                rowsum = rowsum + cell*cellnum
            else:
                rowsum = rowsum + random.uniform(0,1)
            Y.itemset((rownum,0),rowsum)
            cellnum = cellnum + 1
        rownum = rownum + 1
    return pd.DataFrame(Y, columns=['pred_val'])



