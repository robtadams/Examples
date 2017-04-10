# solutions.py
# Robert Adams
# Andre Judson

import cmath

debug = False


def fft(arr):
    global debug

    n = len(arr)
    omega = cmath.e ** (2 * cmath.pi * 1j / n)

    r = local_fft(arr, omega)

    for i in range(1, len(r) // 2):
        r[i], r[-i] = r[-i], r[i]

    return r


def local_fft(arr, omega):
    global debug

    # Base case
    # print("arr length: ", len(arr))
    if len(arr) is 1:
        return arr

    even = []
    odd = []

    n = len(arr)

    for i in range(0, n):
        if i % 2 is 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    s = local_fft(even, omega ** 2)
    sprime = local_fft(odd, omega ** 2)

    r = [0] * n

    j = 0
    while True:
        if j > ((n // 2) - 1):
            break
        r[j] = s[j] + (omega ** j) * sprime[j]
        r[j + n // 2] = s[j] - (omega ** j) * sprime[j]

        j += 1

    return r


def ifft(arr):
    global debug

    n = int(len(arr))
    r = fft(arr)

    if debug is True:
        print("Old r:", r)

    # Invert list, except index 0, and also divide all elements by n
    for i in range(1, n // 2):
        r[i], r[-i] = r[-i]/n, r[i]/n
    r[n // 2] /= n
    r[0] /= n

    if debug is True:
        print("New r:", r)

    return r


def convolution(arr1, arr2):
    global debug

    for x in range(0, len(arr1)):
        arr1.append(0)
        arr2.append(0)

    if debug is True:
        print()
        print("Arr1: ", arr1)
        print("Arr2: ", arr2)
        print()

    s = fft(arr1)
    sprime = fft(arr2)

    cm = []
    for y in range(0, len(s)):
        # Drop imaginary number at the VERY end
        cm.append(s[y] * sprime[y])

    inverse = ifft(cm)

    if debug is True:
        print("Convolution: [", end='')
        # for z in range(0, len(cm)):
        for z in range(0, len(cm) - 1):
            print(inverse[z].real, end='')
            if z != len(cm) - 2:
                print(", ", end='')

        print("]")

    return inverse


def slow_convolution(a, b):
    global debug

    if debug is True:
        print()
        print("Arr1: ", a)
        print("Arr2: ", b)
        print()

    r = []
    n = len(a)
    for i in range(0, n):
        sum = 0
        for j in range(0, i):
            sum += a[j] * b[i - j]
        r.append(sum)

    return r
