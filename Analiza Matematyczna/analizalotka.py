import matplotlib.pyplot as plt ##biblioteka od tworzenia wykresów 
import numpy as np
import scipy

##https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html

##zmienne które możemy dowolnie modyfikowac  
a=float(input("Podaj a"))
b=float(input("Podaj b"))
d=float(input("Podaj d"))
g=float(input("Podaj g"))
x0=int(input("Podaj ilość drapieżców"))
y0=int(input("Podaj ilość ofiar"))

figure,((ax1),(ax2)) = plt.subplots(2, 1)

def pochodna(X,t,a,b,d,g):
    x, y= X ## przypisanie kolejno x i y  elementów wektora
    dotx=x*(a-b*y)
    doty=y*(-d+g*x)
    return np.array([dotx,doty])


n=1000
tmax=30
t=np.linspace(0,tmax,n) ##generowanie równomiernie rozmieszczonych punktów czasowych w przedziale od 0 do tmax.
X0=[x0,y0] ##lista, która zawiera wartości początkowe dla zmiennych stanu w systemie równań różniczkowych

wynik=integrate.odeint(pochodna,X0,t,args=(a,b,d,g)) #obliczanie całki
x,y = wynik.transpose() ##transponowanie macierzy 


##portret fazowy 
k = np.linspace(1.0, 6.0, 21) ##generowanie równomiernie rozmieszczonych punktów czasowych w przedziale od 1 do 6.
for zajac in k:
    X0 = [zajac, 1.0]
    Xs = integrate.odeint(pochodna, X0, t, args = (a, b, d, g))
    ax2.plot(Xs[:,0], Xs[:,1], "-", label =str(X0[0]))

plt.figure()
ax1.grid()
ax1.plot(t, x, label = 'Ofairy')
ax1.plot(t, y, label = "Drapieżcy")

ax1.set_title("Model Lotki-Volterry")
ax1.set_xlabel("Czas")
ax1.set_ylabel("Populacja")

ax2.set_title("Portret Fazowy")
ax2.set_xlabel("Ofiary")
ax2.set_ylabel("Wilki")

plt.show()