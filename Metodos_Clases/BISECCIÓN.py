#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Importamos librerias
from math import *
import numpy as np
import matplotlib as plt


# In[22]:


# Definimos la función de forma global
def f(x):
    return cos(x)


# In[23]:


# Definiremos la función para la bisección, en esta deberia estar la función f
# sin embargo ya la definimos anteriormente
# Recordar que en el metodo de bisección tomamos un intervalo [a,b]
# para una función f(x) donde f(a) y f(b) son signos contrarios

def bisección(a,b,tol):
    m1=a
    m=b
    k=0
    if(f(a)*f(b)>0):
        print("La función no cambia de signo, por tanto este metodo es impreciso para hallar raices")
        return

    while(abs(m1-m)>tol):
        m1=m
        m=(a+b)/2
        if(f(a)*f(m)<0): #La función cambia de signo en el intervalo [a,m]
            b=m
        if(f(m)*f(b)<0): #La función cambia de signo en el intervalo [m,b]
            a=m
        print("El intervalo es [" , a , "," , b , "]")
        k=k+1;
        
        
    print ("Pasadas", k, "interaciones se obtiene que", m, "es una buena aproximación")
    

bisección(0, pi, 10**(-6))
        


# In[ ]:




