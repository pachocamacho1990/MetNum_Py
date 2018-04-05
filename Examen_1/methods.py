import math as m
import sympy as sp
import numpy as np 

def biseccion(a,b,f,tipo):
    # se aproxima el cero de f dentro del 
    # intervalo (a,b) usando un esquema de 
    # iteracion dado por el "flag" tipo:
    # tipo -> (nsteps [0], epsilon [1])
    if f(a)*f(b) > 0:
        print('el intervalo no contiene un cero de la funcion')
        return None
    else:
        if tipo==0:
            nsteps = int(input('seleccione el numero de iteraciones: '))
            for i in range(nsteps+1):
                c = (a+b)/2
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c
            return c
        elif tipo==1:
            epsilon = float(input('seleccione el error permitido: '))
            while (b-a)/2 > epsilon:
                c = (a+b)/2
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c
            return c

def regula_falsi(a,b,f,tipo):
    if f(a)*f(b) > 0:
        print('el intervalo no contiene un cero de la funcion')
        return None
    else:
        if tipo==0:
            nsteps = int(input('seleccione el numero de iteraciones: '))
            for i in range(nsteps+1):
                c = a - f(a)*(b-a)/(f(b)-f(a))
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c
            return c
        elif tipo==1:
            epsilon = float(input('seleccione el error permitido: '))
            while (b-a)/2 > epsilon:
                c = a - f(a)*(b-a)/(f(b)-f(a))
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c
            return c
        
def newton(f,x0,niter):
    x = sp.symbols('x')
    def df(x):
        return sp.diff(f(x),x)
    DerivF = sp.lambdify(x,df(x),'numpy')
    xold = x0
    for i in range(niter):
        xnew = xold - f(xold)/DerivF(xold)
        xold = xnew
        
    return xnew

def secante(f,x0,x1,niter):
    xold1 = x0
    xold2 = x1
    for i in range(niter):
        xnew = xold1 - f(xold1)*(xold2-xold1)/(f(xold2)-f(xold1))
        xold2 = xold1
        xold1 = xnew
        
    return xnew

def root(a,b,f,niter,method):
    if f(a)*f(b) > 0:
        print('el intervalo no contiene un cero de la funcion')
        return None
    else:
        for i in range(niter+1):
            if method=='biseccion':
                c = (a+b)/2
            elif method=='regula-falsi':
                c = a - f(a)*(b-a)/(f(b)-f(a))
            else:
                print('ERROR: metodo no implementado')
                return None
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
        return c