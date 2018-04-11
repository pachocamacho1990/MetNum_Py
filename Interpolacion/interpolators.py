# ---------------------------------------------------------------------
# Compendio de programas.
# Matemáticas para Ingeniería. Métodos numéricos con Python.
# Copyright (C) 2017  Los autores del texto.
# ---------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# ---------------------------------------------------------------------
# Version modificada por Francisco J. Camacho (2018)
# ---------------------------------------------------------------------

from math import *

def LagrangePol(datos):

    def L(k, x):  # pol $L_k(x)=\prod\limits_{i \neq k}\frac{x-x_i}{x_k-x_i}$
        out = 1.0
        for i, p in enumerate(datos):
            if i != k:
                out *= (x-p[0])/(datos[k][0]-p[0])
        return out

    def P(x):  # polinomio $P(x)=\sum\limits_{k}f(x_k)L_k(x)$
        lag = 0.0
        for k, p in enumerate(datos):
            lag += p[1]*L(k, x)
        return lag

    return P

def CubicSplines(datos):
    n = len(datos)-1
    # Inicializar vectores auxiliares
    A = [x[1] for x in datos]
    X = [x[0] for x in datos]
    H = [0.0 for x in range(n)]
    B = [0.0 for x in range(n+1)]
    C = [0.0 for x in range(n+1)]
    D = [0.0 for x in range(n+1)]
    alpha = [0.0 for x in range(n)]
    mu = [0.0 for x in range(n+1)]
    l = [1.0 for x in range(n+1)]
    z = [0.0 for x in range(n+1)]

    # Crear vector $H$
    for i in range(n):
        H[i] = X[i+1]-X[i]

    # Crear vector $\alpha$
    for i in range(1, n):
        alpha[i] = (3.0/H[i])*(A[i+1]-A[i])-(3.0/H[i-1])*(A[i]-A[i-1])

    # Solucionar sistema tridiagonal
    for i in range(1, n):
        l[i] = 2.0*(X[i+1]-X[i-1])-H[i-1]*mu[i-1]
        mu[i] = float(H[i])/l[i]
        z[i] = (alpha[i]-H[i-1]*z[i-1])/float(l[i])

    # Solucionar sistema tridiagonal
    for j in range(n-1, -1, -1):
        C[j] = z[j]-mu[j]*C[j+1]
        B[j] = (A[j+1]-A[j])/float(H[j])-H[j]*(C[j+1]+2*C[j])/3.0
        D[j] = (C[j+1]-C[j])/(3.0*H[j])

    # Retornar vectores $A$, $B$, $C$, $D$
    return A[:-1], B[:-1], C[:-1], D[:-1]

def CSpol(datos,debug=False):

    # Funcion que indica si un valor x 
    # esta en el intervalo [min,max)
    def checkInterval(x0,min,max):
        if x0 >= min:
            if x0 < max:
                return True
            else:
                return False
        else:
            return False

    def intervalIndex(x,datos):
        # out  =  0 (dentro del intervalo)
        #      =  1 (a la derecha del intervalo)
        #      = -1 (a la izquierda del intervalo)
        n = len(datos)-1;
        if checkInterval(x,datos[0][0],datos[-1][0]):
            out = 0;
            for i, p in enumerate(datos):
                if checkInterval(x,datos[i][0],datos[i+1][0]):
                    isel = i;
                    return isel, out
        else:
            if x >= datos[-1][0]:
                out = 1;
                isel = n-1;
                return isel, out
            elif x < datos[0][0]:
                out = -1;
                isel = 0;
                return isel, out 

    def interval(x):
        index, out = intervalIndex(x,datos);
        if out == 0:
            print('el valor de x  = '+str(x)+' se encuentra en el intervalo:')
            print(datos[index][0],datos[index+1][0])
        elif out == 1:
            print('el numero esta a la derecha del intervalo')
        elif out == -1:
            print('el numero esta a la izquierda del intervalo')

    [A,B,C,D] = CubicSplines(datos);

    def s(x):
        if debug==True:
            interval(x)
        j, out = intervalIndex(x,datos);
        xj = datos[j][0];
        return A[j] + B[j]*(x-xj) + C[j]*pow(x-xj,2) + D[j]*pow(x-xj,3)


    return s

def NewtonPol(dat):
    n = len(dat)-1
    F = [[0 for x in dat] for x in dat]  # crear tabla nula

    for i, p in enumerate(dat):  # condiciones iniciales
        F[i][0] = p[1]

    for i in range(1, n+1):  # tabla de diferencias divididas
        for j in range(1, i+1):
            F[i][j] = (F[i][j-1]-F[i-1][j-1])/(dat[i][0]-dat[i-j][0])

    def L(k, x):  # polinomio $L_k(x)=\prod\limits_{i \leq k}(x-x_i)$
        out = 1.0
        for i, p in enumerate(dat):
            if i <= k:
                out *= (x-p[0])
        return out

    def P(x):  # $P(x)=f[x_0]+\sum_{k=1}^{n}f[x_0,x_1,\ldots,x_k]L_{k-1}(x)$
        newt = 0.0
        for i in range(1, n+1):
            newt += F[i][i]*L(i-1, x)
        return newt + F[0][0]

    return F, P
