#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
import Tkinter as Tk
import numpy.random as random


root = Tk.Tk()
root.wm_title("Metoda Monte Carlo")
f = Figure(figsize=(6, 6),dpi=100)
a = f.add_subplot(111)
w = Tk.Label(root, text=" ")
q = Tk.Label(root, text=" ")
def koniec():
        root.quit()
        root.destroy()
def montecarlo(b):
    a=np.linspace(1,b,b)
    suma=0.0
    listax=[]
    listay=[]
    for c in a :
        x=random.rand()*2-1
        y=random.rand()*2-1
        listax.append(x)
        listay.append(y)
    return zip(listax,listay)        
def pii(b):
    suma=0.0
    for a in b:
       if a[0]*a[0]+a[1]*a[1] < 1:
            suma=suma+1
    return (4*suma/len(b))

def rysuj(e):
  for c in e:
      if np.sqrt(c[1]*c[1]+c[0]*c[0])<1:
          a.scatter(c[0],c[1],color="red")
      else:
          a.scatter(c[0],c[1],color="blue")
  x=np.linspace(-1,1,500)
  y1=[]
  y2=[]
  for c in x:
    y1.append(np.sqrt(1-c*c))
    y2.append(-np .sqrt(1-c*c))
  k=np.linspace(1,1,500)
  l=np.linspace(-1,-1,500)
  m=np.linspace(-1,1,500)
  a.plot(k,m,color="black",linewidth="2")
  a.plot(m,k,color="black",linewidth="2")
  a.plot(l,m,color="black",linewidth="2")
  a.plot(m,l,color="black",linewidth="2")
  a.plot(x,y1,color="green",linewidth="2")
  a.plot(x,y2,color="green",linewidth="2")


def rob(n):
    t=montecarlo(n)
    w.config(text="Wynikiem jest " + str(pii(t)))
    q.config(text=u"Błąd wynosi " + str(np.abs((pii(t)-np.pi))))
    rysuj(t)
def rob100():
    a.clear()
    rob(100)
    canvas.show()
def rob500():
    a.clear()
    rob(500)
    canvas.show()
def rob1000():
    a.clear()
    rob(1000)
    canvas.show()
def rob2000():
    a.clear()
    rob(2000)
    canvas.show()


i=(0,0)
canvas = FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.grid(row=0,column=0,rowspan=5,columnspan=4)
button1 = Tk.Button(root, text='1000', command=rob1000).grid(row=5,column=2)
button2 = Tk.Button(root, text='100', command=rob100).grid(row=5,column=0)
button3 = Tk.Button(root, text='2000', command=rob2000).grid(row=5,column=3)
button4 = Tk.Button(root, text='500', command=rob500).grid(row=5,column=1)
button = Tk.Button(root, text='Quit', command=koniec).grid(row=6,column=3)
w.grid(row=6,column=0)
q.grid(row=6,column=1)
rob1000()
Tk.mainloop()
