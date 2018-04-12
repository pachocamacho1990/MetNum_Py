import numpy as np
import math as mt

# clase que cálcula todas las sumatorias del 
# metodo de regresion lineal.
class totals(object):
    def __init__(self,data):
        [X,Y,XX,YY,XY] = [0.0,0.0,0.0,0.0,0.0]
        for p in data:
             X += p[0]
             Y += p[1]
             XX += pow(p[0],2.0)
             YY += pow(p[1],2.0)
             XY += p[0]*p[1]
        self.X = X
        self.Y = Y
        self.XX = XX
        self.YY = YY
        self.XY = XY
        self.m = len(data)

# funcion que calcula el modelo lineal
# usando minimos cuadrados.
def mincua_linear(cfs):
    # cfs is an instance of 
    # class "totals" for the 
    # data in study
    def linear(x):
        a0 = (cfs.Y*cfs.XX-cfs.X*cfs.XY)/\
                (cfs.m*cfs.XX-pow(cfs.X,2))
        a1 = (cfs.m*cfs.XY-cfs.X*cfs.Y)/\
                (cfs.m*cfs.XX-pow(cfs.X,2))
        return a0+a1*x
    return linear

# funcion que calcula el coeficiente de correlacion
def r2(cfs):
    return (cfs.m*cfs.XY-cfs.X*cfs.Y)\
            /(mt.sqrt((cfs.m*cfs.XX-pow(cfs.X,2))\
            *(cfs.m*cfs.YY-pow(cfs.Y,2))))

import pandas as pd
def reshape_data(x,y,df):
    # df     -> dataframe from pandas
    # x(str) -> column name acting as x variable
    # y(str) -> column name acting as y variable
    rs_dat = []
    for i in range(len(df)):
        rs_dat.append((df.iloc[i][x],df.iloc[i][y]))
    return rs_dat

