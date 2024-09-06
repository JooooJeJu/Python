import matplotlib.pyplot as plt ##biblioteka od tworzenia wykresów 


"""
x[n+1]=x[n]+(h/6)*(m1+2m2+2m3+m4)
y[n+1]=y[n]+(h/6)*(k1+2k2+2k3+k4)

m1=f(x[n],y[n])
k1=g(x[n],y[n])

m2=f(x[n]+((1/2)*h)*m1,y[n]+((1/2)*h)*k1)
k2=g(x[n]+((1/2)*h)*m1,y[n]+((1/2)*h)*k1)

m3=f(x[n]+((1/2)*h)*m2,y[n]+((1/2)*h)*k2)
k3=g(x[n]+((1/2)*h)*m2,y[n]+((1/2)*h)*k2)

m4=f(x[n]+h*m3,y[n]+h*k3)
k4=g(x[n]+h*m3,y[n]+h*k3)

"""



## return (2*a)+(4*b)   a+b
## return -a+(6*b)      -5*a-b 
## h=0.05 t<1


##x'=x+y --> f()
##y'=-5x-y --> g()

def f(a,b):
    return a+b
def g(a,b):
    return -5*a-b

n=int(input("Podaj ile chcesz wyświetlić kolejnych rozwiązań równania: "))
x0=float(input("Podaj miejsce zerowe x(x(0)=" "): "))
y0=float(input("Podaj miejsce zerowe y(y(0)=" "): "))
h=float(input("Podaj odstęp czasu(h): "))
t=0

listax=[]
listay=[]
listat=[]
listat.append(t)

while t<n:
    m1=f(x0,y0)
    k1=g(x0,y0)
    
    x2=x0+((1/2)*h)*m1
    y2=y0+((1/2)*h)*k1
    
    m2=f(x2,y2)
    k2=g(x2,y2)
    
    x3=x0+((1/2)*h)*m2
    y3=y0+((1/2)*h)*k2
    
    m3=f(x3,y3)
    k3=g(x3,y3)
    
    x4=x0+h*m3
    y4=y0+h*k3
    
    m4=f(x3,y3)
    k4=g(x4,y4)
    
    t=t+h 
    x0=x0+(h*(1/6)*(m1+(2*m2)+(2*m3)+m4))
    y0=y0+(h*(1/6)*(k1+(2*k2)+(2*k3)+k4))
    
    listax.append(x0)
    listay.append(y0)
    listat.append(t) ## do wykresu punktowego (scatter) potrzebuje dwóch argumentów, w tym przypadku t lub x/y jeśli fazowy
    

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax2.plot(listax)    ## jeśli wykres punktowy to ax2.scatter(listat,listax)
ax4.plot(listay)    ## jeśli wykres punktowy to ax2.scatter(listat,listay)
ax1.plot(listax,listay)     ## fazowy
ax3.plot(listax)
ax3.plot(listay)

plt.show()