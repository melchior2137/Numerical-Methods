import time # mierzenie czasu
import matplotlib.pyplot as plt #wykres
import math #floor

def backward_subs(A, y):
    x = [y[N-1]/A[0][N-1]]
    for i in range(0, N-1):
        x.append((y[N-2-i] - A[1][N-i-2]*x[i])/A[0][N-i-2])
    x.reverse()
    return x

def multiply_vectors_hxv(horizontal, vertical):
    result = 0
    for i in range(0, N):
        result += horizontal[i]*vertical[i]
    return result

def subtract_vectors(x,y):
    x_temp = list(x)
    for i in range(0, N):
        x_temp[i] -= y[i]
    return x_temp

def multiply_vector(x, multiplier):
    x_temp = list(x)
    for i in range(0, N):
        x_temp[i] *= multiplier
    return x_temp

def f(N):
    start = time.time()

    # Macierz A
    A = [[9]*N, [7]*(N-1)]
    # Wektor u
    u = [1]*N
    # Wektor v^T
    vT = [1]*N
    # Wektor b^T
    bT = [5] * N

    # Wyliczanie z
    z = backward_subs(A, bT)

    # Wyliczanie x
    x = backward_subs(A, u)

    # Wyliczanie y
    y = subtract_vectors(z, multiply_vector(x, (multiply_vectors_hxv(vT, z) / (1 + multiply_vectors_hxv(vT, x)))))

    end = time.time()
    return (end - start)*1000



N = 100
u_size = []
u_time = []
while N <= 1500000:
    u_size.append(N)
    u_time.append(f(N))
    N *= 1.15
    N = math.floor(N)

plt.plot(u_size, u_time, color='maroon')
plt.ylabel("Czas wykonania")
plt.xlabel("Rozmiar macierzy")
plt.title("Zadanie numeryczne 4")
plt.show()