import numpy as np


def main():
    A1 = np.array([[2.34332898, -0.11253278, -0.01485349, 0.33316649, 0.71319625],
                   [-0.11253278, 1.67773628, -0.32678856, -0.31118836, -0.43342631],
                   [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
                   [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
                   [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])
    A2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
                   [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
                   [0.00237792, -0.70698859, 2.54906441, 0.87863502, 0.07309288],
                   [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
                   [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])

    b1 = np.array([
        [3.55652063354463],
        [-1.86337418741501],
        [5.84125684808554],
        [-1.74587299057388],
        [0.84299677124244]])

    b2 = b1 + np.array([[0.00001],
                        [0],
                        [0],
                        [0],
                        [0]])


    Y1 = np.linalg.solve(A1, b1)
    Y2 = np.linalg.solve(A2, b1)

    YPRIM1 = np.linalg.solve(A1, b2)
    YPRIM2 = np.linalg.solve(A2, b2)

    D1 = np.linalg.norm(Y1 - YPRIM1)
    D2 = np.linalg.norm(Y2 - YPRIM2)

    # print("Y1: ",Y1,"\nY2: ", Y2)
    # print("Y1PRIM: ",YPRIM1,"\nY2PRIM: ", YPRIM2)
    # print("Pierwsza delta: ",D1, "\nDruga delta: ",D2)

    #wartosci wlasne do Kappy
    A1MaxEig = max(np.linalg.eigvals(A1))
    A1MinEig = min(np.linalg.eigvals(A1))
    A2MaxEig = max(np.linalg.eigvals(A2))
    A2MinEig = min(np.linalg.eigvals(A2))

    # print(A1MaxEig, A1MinEig, A1MaxEig/A1MinEig)
    # print(A2MaxEig, A2MinEig, A2MaxEig/A2MinEig)


if __name__ == "__main__":
    main()
