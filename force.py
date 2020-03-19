from main import gen, div
import numpy as np

m = [0,1,1,1]
g = [1, 1, 1, 0, 1]
d = 3

code = gen(m, g, len(g) - 1)
lenC = len(code)
print(code, div(code.copy(), g))

print("start search...")
for i in range(2 ** len(code)):
    n = list('{0:b}'.format(i))
    # print(m)
    n = np.array(['0'] * (lenC - len(n)) + n).astype("int32")
    n = list(n)
    #print(n)
    code_noise = np.bitwise_xor(code.copy(), n)
    #code = gen(m, g, len(g) - 1)
    result = div(code_noise.copy(), g)

    if np.sum(result) == 0:
        if np.sum(n) <= d - 1 and np.sum(n) >= 1:
            print("message ", m, "code ", code_noise, "noise ", n, "result ", result, np.sum(n))
