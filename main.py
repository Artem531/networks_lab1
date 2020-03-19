import numpy as np
import matplotlib.pyplot as plt

from math import factorial as fac

def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

def find(m):
    for i, val in enumerate(m):
        if val == 1:
            return len(m) - i - 1
    return 0

def div(a, mod):
    for i, val in enumerate(a):
        if val == 1:
            if find(a) >= find(mod):
                dif = (len(a) - i) - len(mod)
                a[i:i + len(mod) + dif] = np.bitwise_xor(a[i:i + len(mod) + dif], np.array(mod + [0] * dif))
            else:
                break
    return a

# a = np.array([1,0,1,1])
# b = np.array([1,1,1])
# print(div(a, b))


def rotate(arr, bits):
    lenA = len(arr)
    arr = arr + [0] * bits
    return arr

def gen(m, g, r):
    #powM = find(m)
    dif = r
    shifted = np.array(rotate(m, dif))
    c = div(shifted.copy(), g)
    code = np.bitwise_xor(shifted, c)
    return code
#
# print(gen([0,1,1], g, len(g) - 1))
def main():
    n = 7
    # k = 4
    # r = 4
    # d = 3
    #
    # g = [1, 0, 1, 1]

    k = 3
    g = [1, 1, 1, 0, 1]
    d = 4

    stat = [0] * (n + 1)

    for i in range(2**k):
        m = list('{0:b}'.format(i))
        #print(m)
        m = np.array(['0'] * (k - len(m)) + m).astype("int32")
        m = list(m)
        #print(m)
        code = gen(m, g, len(g) - 1)
        print(m, code, div(code.copy(), g))
        stat[sum(code)] += 1
    print(stat)

    stat = np.array(stat)
    result = []
    for p in np.linspace(0.1, 1, 100):
        i = d
        res = 0
        for ai in stat[d:]:
            if p == 1:
                f = 0
            res += ai * p ** i * (1 - p) ** (n - i)
            i = i + 1
        result.append(res)
        #print(p_arr)

    result_upperb = []
    stat = np.array([binomial(n, x) for x in range(0, d)])

    for p in np.linspace(0.1, 1, 100):
        i = 0
        res = 0
        for ai in stat:
            if p == 1:
                f = 0
            res += ai * p ** i * (1 - p) ** (n - i)
            i = i + 1
        result_upperb.append(1 - res)
        #print(p_arr)

    plt.plot(np.linspace(0.1, 1, 100), result, "*")
    #plt.show()
    plt.plot(np.linspace(0.1, 1, 100), result_upperb, "-")
    plt.show()

if __name__ == '__main__':
    main()
