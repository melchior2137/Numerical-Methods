import math
import numpy as np
import matplotlib.pyplot as plt
import numpy.random

n = 100
mu = 0

# a,b,c,d = -3, 2.3, 5.3, 10

def wartosc_funkcji(wspolczynniki, x):
    a,b,c,d = wspolczynniki
    return a*pow(x, 9/8) + b*math.sin(3*x) + c * math.log2(2*x) + d * pow(math.cos(x), 3)

def generowanie_danych(szum=0, funkcja = 0, sigma=0):
    coeff = [-3, 2.3, 5.3, 10]
    X = []
    Y = []
    i = 10
    while(i <= 20):
        X.append(i)
        if(szum):
            temp = wartosc_funkcji(coeff, i) + numpy.random.normal(mu, sigma)
        else:
            temp = wartosc_funkcji(coeff, i)
        Y.append(temp)
        if(funkcja):
            i+=0.1
        else:
            i+=10/n
    return [X, Y]

def stworzenie_macierzy(X,Y):
    A = []
    for x in X:
        A.append([pow(x, 9/8), math.sin(3*x), math.log2(2*x), pow(math.cos(x), 3)])
    return A

def oblicz_wspolczynniki(A, Y):
    # rozklad svd
    u, s, v = np.linalg.svd(A)

    # stworzenie macierzy sigma
    ushape = u.shape
    sigma = np.zeros((4, ushape[0]))
    for i in range(s.size):
        if (s[i] > 0):
            sigma[i][i] = 1 / s[i]
        else:
            sigma[i][i] = 0

    # pseudoodwrotnosc macierzy A
    Aplus = np.matmul(np.matmul(np.transpose(v), sigma), np.transpose(u))

    wspolczynniki = np.matmul(Aplus, Y)
    return wspolczynniki


def main():
    sigma = 10
    # title = "mu = {}, sigma = {} n = {}.".format(mu, sigma, n)
    X, Y = generowanie_danych(0, 1, sigma)
    plt.plot(X, Y, label='G(x)', linewidth=5)
    for i in range(4):
        X, Y = generowanie_danych(0,0, sigma)
        # plt.scatter(X,Y, color='blue', label='Bez szumu')
        X, Y = generowanie_danych(1, 0, sigma)
        # plt.scatter(X,Y, color='red', label='Z szumem')

        A = numpy.array(stworzenie_macierzy(X,Y))

        wspolczynniki = oblicz_wspolczynniki(A, Y)
        print(wspolczynniki)

        argumenty = []
        wartosci = []
        i = 10
        while (i <= 20):
            argumenty.append(i)
            wartosci.append(wartosc_funkcji(wspolczynniki, i))
            i += 10/n
        aproksymacja = "mu = 0, sigma = {}".format(sigma)
        plt.plot(argumenty,wartosci, label=aproksymacja)


        sigma*=2
        i+=1

    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xscale('log')
    # plt.yscale("log")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()

