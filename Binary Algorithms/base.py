# base.py
# Robert Adams
# Andre Judson

import random
import sys
import time
import solutions

sys.setrecursionlimit(10000000)

from random import *


def shift(A, n):
    if n == 0:
        return A
    return [0] + shift(A, n - 1)


def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))
    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))


def Mult(X, Y):
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1, Y1))


def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True


def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]

def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def TwosComp(A):
    return local_add(solutions.flipbits(A), [1, 0])
    #return add(solutions.flipbits(A), [1, 0])

def add(A, B):
    # If both A and B are positive
    if A[-1] == 0 and B[-1] == 0:
        ret = local_add(A, B)
        ret.append(0)
        return ret

    # If both A and B are negative
    if A[-1] == 1 and B[-1] == 1:
        A1 = TwosComp(A)
        B1 = TwosComp(B)
        ret = TwosComp(local_add(A1, B1))
        ret.append(1)
        return ret

    ret=local_add(A,B)
    if compare(A, B) == 1:
        ret.pop()
    return ret


def local_add(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)

    #if B1 == [1]:
    #    B1 = [1,0]

    if n < m:
        for j in range(len(B1) - len(A1)):
            if A1[-1] == 0:
                A1.append(0)
            else:
                A1.append(1)
    else:
        for j in range(len(A1) - len(B1)):
            if B1[-1] == 0:
                B1.append(0)
            else:
                B1.append(1)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C


def Add(A, B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))


def exc_or(a, b, c):
    if isinstance(a, list):
        print("A:", a, ", B:", b, ", C:", c)
        #return(a[0] ^ (b ^ c))
    return (a ^ (b ^ c))


def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0


def bin2dec(A):

    negative = False

    ##############
    if A[-1] == 0:
        #A.pop(-1)
        A.pop()
    else:
        negative = True
        A = solutions.flipbits(A)
        A = local_add(A, [1, 0])
        A.pop()
        #A.pop(-1)
    ##############

    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    if negative == False:
        return val
    else:
        return (val * -1)

def reverse(A):
    B = A[::-1]
    return B


def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B

    # If this is pass by reference then fix this
    ###################
    if A[-1] == 1:
        A = TwosComp(A)
    if B[-1] == 1:
        B = TwosComp(B)
    ####################
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0


def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))

def dec2bin(n):
    if n < 0:
        A = local_dec2bin(n)
        temp = TwosComp(A)
        temp.append(1)
        return temp

    temp = local_dec2bin(n)
    temp.append(0)
    return temp

def local_dec2bin(n):
    if n == 0:
        #return []
        return []
    # m = n / 2
    m = n // 2
    A = local_dec2bin(int(m))
    fbit = n % 2
    return [fbit] + A

# X = 2; Y = 1 // ([1], [0]) // ([1], [0]) + ([1], [0]) = ([2], [0]) //
# X = 1; Y = 1 // ([], []) + ([], []) = ([], []) // ([0], [1]) // ([1], [0])
# X = 0; Y = 1 // ([], [])
def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        #return ([], [])
        #print ("divide: X is", X, "(should be zero)")
        return ([0], [0])
    #print ("divide: calling recursive on ", X, "and", Y)
    (q, r) = divide(div2(X), Y)
    #print ("divide: Y is", Y)

    #print ("q: ", q)
    q = add(q, q)
    #print ("q: ", q)

    #print ("r: ", r)
    r = add(r, r)
    #print ("r: ", r)


    if (not even(X)):
        #print ("divide: X is not even")
        r = add(r, [1, 0])


    if (not compare(r, Y) == 2):
        #print ("divide: r is greater than or equal to Y")


        #print ("r: ", r)
        #print ("Y: ", Y)
        #print ("divide: Subtracting Y from r")
        # May not work
        r = solutions.sub(r, Y)
        r.pop()
        #print ("r: ", r)
        #print ("Y: ", Y)


        #print ("divide: Adding one to quotient")
        #print ("q: ", q)
        q = add(q, [1, 0])
        #print ("r: ", r)

    #print ("returning q and r")
    #print ("q: ", q)
    #print ("r: ", r)

    return (q, r)


def Divide(X, Y):
    num = dec2bin(X)
    den = dec2bin(Y)

    return divide(num, den)


def map(v):
    if v == []:
        return '0'
    elif v == [0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0, 1]:
        return '2'
    elif v == [1, 1]:
        return '3'
    elif v == [0, 0, 1]:
        return '4'
    elif v == [1, 0, 1]:
        return '5'
    elif v == [0, 1, 1]:
        return '6'
    elif v == [1, 1, 1]:
        return '7'
    elif v == [0, 0, 0, 1]:
        return '8'
    elif v == [1, 0, 0, 1]:
        return '9'


def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0, 1, 0, 1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))