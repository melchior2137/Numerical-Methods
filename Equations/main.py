import math
import matplotlib.pyplot as plt

eps = 10e-10
x0 = math.log(2, math.e)
MAX_ITERATIONS = 40


def wartosc_funkcji(x, n):
    if(n == 1):
        return math.pow(math.exp(x) - 2, n)
    else:
        return (math.exp(x) - 2) / (n * math.exp(x))

def bisekcja(n, a, b):
    ilosc_krokow = 0
    kroki = []
    dokladnosc = []

    y_a = wartosc_funkcji(a, n)
    y_b = wartosc_funkcji(b, n)
    if y_a * y_b >= 0:
        return "Nie można zastosować metody bisekcji", 0, 0, 0

    c = (a + b) / 2
    for x in range(MAX_ITERATIONS):
        if (abs(a - b) < eps):
            break
        ilosc_krokow += 1
        kroki.append(ilosc_krokow)
        dokladnosc.append(abs(x0 - c))

        y_a = wartosc_funkcji(a, n)
        y_b = wartosc_funkcji(b, n)
        c = (a + b) / 2
        y_srodek = wartosc_funkcji(c, n)
        if (y_srodek == 0):
            break;
        if y_srodek * y_a < 0:
            b = c
        else:
            a = c

    return c, ilosc_krokow, kroki, dokladnosc


def falsi(n, a, b):
    ilosc_krokow = 0
    kroki = []
    dokladnosc = []

    y_a = wartosc_funkcji(a, n)
    y_b = wartosc_funkcji(b, n)
    if y_a * y_b >= 0:
        return "Nie można zastosować metody falsi", 0, 0, 0

    c = (y_b * a - y_a * b) / (y_b - y_a)
    y_c = wartosc_funkcji(c, n)

    for x in range(MAX_ITERATIONS):
        ilosc_krokow += 1
        kroki.append(ilosc_krokow)
        dokladnosc.append(abs(x0 - c))

        if (abs(y_c) < eps):
            break
        y_a = wartosc_funkcji(a, n)
        y_b = wartosc_funkcji(b, n)
        c = (y_b * a - y_a * b) / (y_b - y_a)
        y_c = wartosc_funkcji(c, n)
        if (y_c == 0):
            break;
        if (y_c * y_a < 0):
            b = c
        else:
            a = c
    return c, ilosc_krokow, kroki, dokladnosc


def sieczne(n, a, b):
    ilosc_krokow = 0
    kroki = []
    dokladnosc = []

    for x in range(MAX_ITERATIONS):
        y_a = wartosc_funkcji(a, n)
        y_b = wartosc_funkcji(b, n)
        c = (y_b * a - y_a * b) / (y_b - y_a)
        y_c = wartosc_funkcji(c, n)

        a = b
        b = c

        if abs(b - a) < eps:
            return c, ilosc_krokow, kroki, dokladnosc

        ilosc_krokow += 1
        kroki.append(ilosc_krokow)
        dokladnosc.append(abs(x0 - c))

    return c, ilosc_krokow, kroki, dokladnosc


def pochodna(x, n):
    if n == 1:
        wynik = math.exp(x)
    if n == 2:
        wynik = math.exp(-x)
    if n == 3:
        wynik = 2 * math.exp(-x) / 3

    return wynik


def newton(n, a):
    ilosc_krokow = 0
    x = a
    kroki = []
    dokladnosc = []
    for m in range(MAX_ITERATIONS):
        ilosc_krokow += 1
        x_new = x - (wartosc_funkcji(x, n) / pochodna(x, n))

        kroki.append(ilosc_krokow)
        dokladnosc.append(abs(x0 - x_new))

        if abs(x_new - x) < eps:
            return x_new, ilosc_krokow, kroki, dokladnosc
        x = x_new
    return x, ilosc_krokow, kroki, dokladnosc


def main():
    print("x0 = ln 2 = ", x0)
    a = 0
    b = 1
    for n in range(1, 4):
        plt.xlabel = "Ilośc kroków"
        plt.ylabel = "Dokładność"
        plt.title("Dla n = {} ".format(n))

        wynik, ilosc_krokow, kroki, dokladnosc = bisekcja(n, a, b)
        plt.plot(kroki, dokladnosc, label='Bisekcja')
        print("Bisekcja dla n =", n, "wynik: ", wynik, " Ilosc krokow: ", ilosc_krokow)

        wynik, ilosc_krokow, kroki, dokladnosc = falsi(n, a, b)
        plt.plot(kroki, dokladnosc, label='Falsi')
        print("Falsi dla n =", n, "wynik: ", wynik, " Ilosc krokow: ", ilosc_krokow)

        wynik, ilosc_krokow, kroki, dokladnosc = sieczne(n, a, b)
        plt.plot(kroki, dokladnosc, label='Metoda siecznych')
        print("Metoda siecznych dla n =", n, "wynik: ", wynik, " Ilosc krokow: ", ilosc_krokow)

        wynik, ilosc_krokow, kroki, dokladnosc = newton(n, a)
        plt.plot(kroki, dokladnosc, label='Newton')
        print("Metoda Newtona dla n =", n, "wynik: ", wynik, " Ilosc krokow: ", ilosc_krokow)

        plt.yscale('log')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()
