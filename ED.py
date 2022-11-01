import numpy as np
import matplotlib.pyplot as plt

#parametros iniciales
dx = 0.2
x0 = 0
y0 = 1
xmax = 2


def f(x,y):
  return (y**2)*np.exp(-x)

Data = np.array([[0,x0,y0,f(x0,y0)]])
total_points = int(np.ceil(xmax/dx))


for k in range(total_points):
  xk = Data[k,1]
  yk = Data[k,2]
  ynext = yk + dx*f(xk,yk)
  xnext = xk+dx

  Data = np.concatenate((Data, np.array([[k+1, xnext, ynext,f(xnext, ynext)]])))


fig = plt.figure(1)
fig.clf()
ax =fig.add_subplot(1,1,1)
ax.plot(Data[:,1], Data[:,2], lw =2, ls ='-', marker='.', ms=8, label='dx = 0.2')
ax.legend()
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')

import numpy as np
import matplotlib.pyplot as plt

### ----- Parámetros ----
dx_list = [0.2,0.1,0.05,0.01]
x0 = 0
y0 = 1
xmax = 2
##-----------------------
def f(x,y):
    return (y**2)*np.exp(-x)

### -- Método de Euler
Data_all = []
for dx in dx_list:
    Data = np.array([[0,x0,y0,f(x0,y0)]])
    total_points = int(np.ceil(xmax/dx))
    for k in range(total_points):
        xk = Data[k,1]
        yk = Data[k,2]
        #------------------------
        xnext = xk + dx
        ynext = yk + dx*f(xk,yk)
        Data = np.concatenate((Data,np.array([[k+1,xnext,ynext,f(xnext,ynext)]])))
        #------------------------
    Data_all.append(Data)
    
#--- Graficación
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(1,1,1)
for k in range(len(Data_all)):
    Data = Data_all[k]
    ax.plot(Data[:,1],Data[:,2],lw=2,ls='-',marker='.',ms=8,
            label=r'$\Delta$'+'x = '+ str(dx_list[k]))
ax.legend()
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
