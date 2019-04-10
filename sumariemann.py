import numpy as np
import matplotlib.pyplot as plt
#Se quiere calcular mediante sumas de Riemman por la izquierda la integral de sqrt(arctan(x))

def riemannplot(f, a, b, ra, rb, n):
    # f es la función 
    # a y b son los limites del eje x para graficar la funcion f
    # ra y rb son los limites del intervalo en el eje x del que queremos calcular la suma
    # n es el numero de rectangulos que calcularemos

    atenuacion = (b-a)/100
    x = np.arange(a, b+atenuacion, atenuacion)
    
    plt.plot(x, f(x), color='red')

    delta_x = (rb-ra)/n
    riemannx = np.arange(ra, rb, delta_x)
    riemanny = f(riemannx)
    riemann_sum = sum(riemanny*delta_x)

    plt.bar(riemannx,riemanny,width=delta_x,alpha=0.5,edgecolor = 'black',facecolor='green')
   
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    plt.title('Suma de Riemann por la izquierde de f(x)')
    plt.figtext(0.1,-0.05, "Suma de Riemann: %.5f " %(riemann_sum), color='b')
    plt.savefig('riemannmedel.png')
    plt.show()


def f(x):
    return np.sqrt(np.arctan(x))
    
riemannplot(f, 0, 1.001, 0, 1.001, 20)
