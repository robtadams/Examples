# main.py
# Robert Adams
# Andre Judson

import solutions
import random
import time


def main():

    print("--- Main Functions ---")
    print("1) Compare: FFT vs. Brute Force Method")
    print("2) Quit")
    print()
    print("--- Test Functions ---")
    print("3) Fast Fourier Transform")
    print("4) Inverse Fast Fourier Transform")
    print("5) Fast Convolution")
    print("6) Brute Force Convolution")
    print("Input: ", end='')
    user = input()

    while user != 2:

        ''' --- Main Functions ---
            1) Compare: FFt vs. Brute Force Method
            2) Quit
        '''

        # 1) Compare: FFT vs. Brute Force Method
        if user == '1':
            print("n = 2 ** k")
            print("Enter a value for K: ", end='')
            k = input()
            k = int(k)

            n = 2 ** k
            n = int(n)

            arr1 = []
            for i in range(0, n):
                arr1.append(random.uniform(0.0, 1.0))

            arr2 = []
            for j in range(0, n):
                arr2.append(random.uniform(0.0, 1.0))

            start = time.clock()
            conv1 = solutions.convolution(arr1, arr2)
            time1 = time.clock() - start

            start = time.clock()
            conv2 = solutions.slow_convolution(arr1, arr2)
            time2 = time.clock() - start

            if len(conv1) < 100:
                print("Fast Fourier Transform Convolution: [", end='')
                # for z in range(0, len(cm)):
                for z in range(0, len(conv1) - 1):
                    print(conv1[z].real, end='')
                    if z != len(conv1) - 2:
                        print(", ", end='')

                print("]")

                print("Brute Force Convolution:           ", conv2)
                print()

            else:
                f = open('out.txt', 'w')
                with open('out.txt', 'w') as f:
                    print('FFT Convolution: ', end='', file=f)
                with open('out.txt', 'a') as f:
                    for z in range(0, len(conv1) - 1):
                        print(conv1[z].real, end='', file=f)
                        if z != len(conv1) - 2:
                            print(", ", end='', file=f)
                    print('', file=f)
                    print('', file=f)
                    print('Brute Force Convolution: ', end='', file=f)
                    print(conv2, file=f)

            print("Time to compute FFT Conv:   ", time1)
            print("Time to compute Brute Conv: ", time2)

        # 2) Quit
        if user == '2':
            return

        ''' --- Test Functions ---
            3) Fast Fourier Transform
            4) Inverse Fast Fourier Transform
            5) Fast Convolution
            6) Brute Force Convolution
        '''

        # 3) Fast Fourier Transform
        if user == '3':
            print("n = 2 ** k")
            print("Enter a value for K: ", end='')
            k = input()
            k = int(k)

            n = 2 ** k
            n = int(n)

            arr1 = []
            for i in range(0, n):
                arr1.append(random.uniform(0.0, 1.0))

            arr2 = []
            for j in range(0, n):
                arr2.append(random.uniform(0.0, 1.0))

            print("Arr1: ", arr1)
            print("FFT:  ", solutions.fft(arr1))
            print()
            print("Arr2: ", arr2)
            print("FFT:  ", solutions.fft(arr2))

        # 4) Inverse Fast Fourier Transform
        if user == '4':

            print("n = 2 ** k")
            print("Enter a value for K: ", end='')
            k = int(input())

            n = 2 ** k

            arr1 = []
            for i in range(0, n):
                arr1.append(random.uniform(0.0, 1.0))

            print("Arr1: ", arr1)
            print("IFFT: ", solutions.ifft(arr1))

        # 5) Fast Convolution
        if user == '5':
            print("n = 2 ** k")
            print("Enter a value for K: ", end='')
            k = input()
            k = int(k)

            n = 2 ** k
            n = int(n)

            arr1 = []
            for i in range(0, n):
                arr1.append(random.uniform(0.0, 1.0))

            arr2 = []
            for j in range(0, n):
                arr2.append(random.uniform(0.0, 1.0))

            solutions.convolution(arr1, arr2)

        # 6) Brute Force Convolution
        if user == '6':
            print("n = 2 ** k")
            print("Enter a value for K: ", end='')
            k = input()
            k = int(k)

            n = 2 ** k
            n = int(n)

            arr1 = []
            for i in range(0, n):
                arr1.append(random.uniform(0.0, 1.0))

            arr2 = []
            for j in range(0, n):
                arr2.append(random.uniform(0.0, 1.0))

            for x in range(0, n):
                arr1.append(0)
                arr2.append(0)

            n *= 2
            print("Convolution: ", solutions.slow_convolution(arr1, arr2))

        print()
        print("Press ENTER to continue ...", end='')
        input()

        print('\n'*100)

        print("--- Main Functions ---")
        print("1) Compare: FFT vs. Brute Force Method")
        print("2) Quit")
        print()
        print("--- Test Functions ---")
        print("3) Fast Fourier Transform")
        print("4) Inverse Fast Fourier Transform")
        print("5) Fast Convolution")
        print("6) Brute Force Convolution")
        print("Input: ", end='')
        user = input()



main()




