import pandas as pd

def equal_operator(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    chkList = ds1 == ds2
    return chkList

def greater_than_operator(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    chkList = ds1 > ds2
    return chkList


def less_than_operator(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    chkList = ds1 < ds2
    return chkList

print equal_operator([2, 4, 6, 8, 10],[1, 3, 5, 7, 10])
print greater_than_operator([2, 4, 6, 8, 10],[1, 3, 5, 7, 10])
print less_than_operator([2, 4, 6, 8, 10],[1, 3, 5, 7, 10])
