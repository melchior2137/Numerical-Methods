import numpy as np
ACCURACY = 1e-9

def QR_method(M):
    iterations = 0;
    while (abs(M[1][0]) > ACCURACY) or (abs(M[2][1]) > ACCURACY) or (abs(M[3][2]) > ACCURACY):
        Q,R = np.linalg.qr(M)
        M = np.matmul(R,Q)
        iterations+=1
    print("Macierz M po przekształceniach QR: \n", M)
    print("Liczba iteracji w metodzie QR: ", iterations)
    eigenvalues = np.diag(M)
    print("Wartosci własne z metody QR: ", eigenvalues)
    return M

def power_method(B):
    yk = np.array([1, 0, 0, 0])
    zk = np.matmul(B, yk)
    yk_prev = yk
    yk = zk / np.linalg.norm(zk)
    iterations = 0

    while(np.linalg.norm(np.subtract(yk_prev, yk)) > ACCURACY):
        yk_prev = yk.copy()
        zk = np.matmul(B, yk)
        yk = zk / np.linalg.norm(zk)
        iterations+=1
    lambda1 = np.linalg.norm(zk)
    print("Macierz B:\n", B)
    print("Moduł największej wartości własnej z metody potęgowej: ", lambda1)
    print("Wektor własny: ", yk)
    print("Liczba iteracji w metodzie potęgowej: ", iterations)



def main():
    M = np.array([[3,6,6,9],
              [1,4,0,9],
              [0, 0.2, 6, 12],
              [0, 0, 0.1, 6]])

    B = np.array([[3,4,2,4],
              [4,7,1,-3],
              [2,1,3,2],
              [4,-3,2,2]])

    numpy_eigvalues_M, numpy_eigvectors_M = np.linalg.eig(M)
    numpy_eigvalues, numpy_eigvectors = np.linalg.eig(B)
    print("Wartosci własne macierzy M z biblioteki numerycznej: \n", numpy_eigvalues_M)
    # print("Wektory własne macierzy M z biblioteki numerycznej: \n", numpy_eigvectors_M)
    print("Wartosci własne macierzy B z biblioteki numerycznej: \n", numpy_eigvalues)
    print("Wektory własne macierzy B z biblioteki numerycznej: \n", numpy_eigvectors)
    print("Macierz M: \n", M)
    QR_method(M)
    power_method(B)


if __name__ == '__main__':
    main()
