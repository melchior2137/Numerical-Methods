import numpy as np  # np.array
import time # mierzenie czasu
import matplotlib.pyplot as plt #wykres


def f(N):
    start = time.time()

    # tworzenie macierzy z zadania
    a = [0.2] * (N - 1)
    b = [1.2] * (N)
    c = []
    for i in range(1, N):
        c.append(0.1 / i)
    d = []
    for i in range(1, N - 1):
        d.append(0.4 / pow(i, 2))
    a.append(0)
    c.append(0)
    d.append(0)
    d.append(0)

    A = np.array([a, b, c, d])

    x = []
    for i in range(0, N):
        x.append(i + 1)

    # print(A)
    # Faktoryzacja LU
    A[0][0] /= A[1][0]
    for i in range(1, N - 1):
        temp = A[0][i - 1] * A[2][i - 1]
        A[1][i] -= temp

        temp = A[0][i - 1] * A[3][i - 1]
        A[2][i] -= temp
        A[0][i] /= A[1][i]

    # ostatni element najdluzszej diagonali
    temp = A[0][N - 2] * A[2][N - 2]
    A[1][N - 1] -= temp

    # print("\n", A)

    #wyznacznik
    if(N == 100):
        sum = 1
        for i in A[1]:
            sum *= i
        print("\nWyznacznik dla N = 100: ", sum)

    # forward substitution dla macierzy L
    z = [1]
    for i in range(1, N):
        temp = (A[0][i - 1] * z[i - 1])
        z.append(x[i] - temp)
    # print(z)

    # backward substitution dla macierzy U
    # najpierw jest jedno rownanie z 1 niewiadoma potem jedno z dwoma i reszta z 3 to wynika z budowy macierzy

    y = [z[N - 1] / A[1][N - 1]]
    y.append((z[N - 2] - A[2][N - 2] * y[0]) / A[1][N - 2])

    j = 0
    for i in range(N - 3, -1, -1):
        y.append((z[i] - (A[3][i] * y[j]) - (A[2][i] * y[j + 1])) / A[1][i])
        j += 1

    y.reverse()
    if(N==100):
        print("Macierz y^T dla N = 100", y)
    end = time.time()
    return (end - start)*1000


def main():
    f(100) #dane z zadania

    #Mierzenie czasu wykonania i rysowanie wykresu
    N = 1000
    size = []
    time = []
    while N <= 10000:
        size.append(N)
        time.append(f(N))
        N+=1000

    plt.bar(size, time, color='maroon',
            width=500)
    plt.ylabel("Czas wykonania")
    plt.xlabel("Rozmiar macierzy")
    plt.title("Zadanie numeryczne 3")
    plt.show()

if __name__ == '__main__':
    main()
