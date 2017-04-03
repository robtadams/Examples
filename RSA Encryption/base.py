# base.py
# Robert Adams
# Andre Judson

import random
import sys
import time
import solutions

sys.setrecursionlimit(10000000)

from random import *

# glo_e = 0

def shift(A, n):
    if n == 0:
        return A
    return [0] + shift(A, n - 1)


def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]

    ### TEMP ###
    if zero(X):
        return [0]
    ############

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
    return local_add(flipbits(A), [1, 0])

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

    if (len(A) == 0):
        return B
    if (len(B) == 0):
        return A

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

    ### TEMP ###
    if len(A) == 0:
        return 0
    ############


    ##############
    if A[-1] == 0:
        #A.pop(-1)
        A.pop()
    else:
        negative = True
        A = flipbits(A)
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

    if (len(A) == 0 and len(B) == 0):
        return 0
    if (len(A) != 0 and len(B) == 0):
        return 1
    if (len(A) == 0 and len(B) != 0):
        return 2

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
        return []
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
        return ([0], [0])
    (q, r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)

    if (not even(X)):
        r = add(r, [1, 0])


    if (not compare(r, Y) == 2):
        r = sub(r, Y)
        r.pop()

        q = add(q, [1, 0])

    return (q, r)


def Divide(X, Y):
    num = dec2bin(X)
    den = dec2bin(Y)

    temp = divide(num, den)

    return bin2dec(list(temp))


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


def fraction_add(P,Q,R,S):
    mult1 = mult(P, S)
    mult2 =mult(Q, R)

    num = add(mult1, mult2)
    den = mult(Q, S)

    return (num, den)


def Sub(A, B):

    a = dec2bin(A)
    b = dec2bin(B)

    return bin2dec(sub(a, b))


def sub(A, B):
    tempA = A[:]
    tempB = B[:]
    return add(tempA, TwosComp(tempB))

def flipbits(A):
    for i in range(len(A)):
        if A[i]:
            A[i] = 0
        else:
            A[i] = 1
    return A

# Precondition: Neither A nor B will be negative
def exponent(A, B):
   if B == []:
       return [1, 0]
   if B == [1, 0]:
       return A
   if B[0] == 0:
       B.pop(0)
       val = exponent(A, B)
       return (mult(val,val))
   else:
       temp = sub(B, [1,0])
       temp.pop(0)
       val = exponent(A, temp)
       return mult(mult(val,val),A)

def Exponent(A, B):
    ret = exponent(dec2bin(A), dec2bin(B))
    return bin2dec(ret)

# Decimal Modular Exponentiation
def Mod_Exp(Base, Exponent, Modulus):

    B = int(Base)
    E = int(Exponent)
    M = int(Modulus)

    if (M == 1):
        return 0
    c = 1
    for e_prime in range(0, E):
        print("e`=", e_prime,".","c=(",c,"*",B,") mod",M,"=",B,"mod",M,"=",(c * B) % M)
        #c = (c * B) % M
        product = Mult(c, B) #Returns as an integer
        c = Mod(product, M)

    return c

# Decimal Modular Exponentiation, but in logarithmic time
def Mod_Exp_Log(Base, Exponent, Modulus):

    B = int(Base)
    E = int(Exponent)
    M = int(Modulus)

    e = dec2bin(E)

    # Base cases
    if M == 0:
        temp = Exponent(B, E)
        # print("Modulus is zero; returning Exponent(", B, ",", E, ") = ", temp)
        return temp
    if M == 1:
        # print("Modulus is one; returning zero")
        return 0

    if E == 0:
        # print("Exponent is zero; returning one")
        return 1
    if E == 1:
        temp = Mod(B, M)
        # print("Exponent is one; returning Mod(", B, ",", M, ") = ", temp)
        return temp

    if B == 0:
        # print("Base is zero; returning zero")
        return 0
    if B == 1:
        # print("Base is one; returning one")
        return 1

    # global glo_e

    # Actual math
    # If the exponent is even ...
    if E % 2 == 0:
        e.pop(0)
        E = bin2dec(e)

        val = Mod_Exp_Log(B, E, M)

        # print("e`=", glo_e, ".", "c=[[(", B, "** (", int(E / 2), ")) mod", M, "] ** 2] mod", M)
        # glo_e += 1

        temp1 = Mult(val, val)
        temp2 = Mod(temp1, M)

        return temp2

    # If the exponent is odd ...
    else:
        e.pop(0)
        E = bin2dec(e)

        val = Mod_Exp_Log(B, E, M)

        # print("e`=", glo_e, ".", "c=(((", B, "** (", int(E / 2), ")) mod", M, ") ** 2) * (", B, "mod", M, ")")
        # glo_e += 1

        temp1 = Mult(val, val)
        temp2 = Mult(temp1, B)
        # temp3 = Mod(temp2, M)
        temp3 = mod(dec2bin(temp2), dec2bin(M))

        return bin2dec(temp3)

# Base is binary
# Exp is decimal
# Modulus is binary


def mod_exp(base, exp, modulus):

    B = bin2dec(base)
    E = int(exp)
    M = bin2dec(modulus)

    if (M == 1):
        return 0
    c = [1,0]
    for e_prime in range(0, E):
        temp_M = modulus
        print("e`=", e_prime,".","c=(",bin2dec(c),"*",B,") mod",M,"=",B,"mod",M,"=", end='')
        #temp = (mult(c, base))
        c = (mult(c, base))
        c = mod(c, temp_M)
        print(bin2dec(c))
    return bin2dec(c)


def gcd(A, B):
    if B > A:
        temp = A
        A = B
        B = temp
    if (A % B) == 0:
        return B

    return gcd(B, A%B)


def Mod(A, B):

    a = dec2bin(A)
    b = dec2bin(B)
    x = mod(a, b)

    return bin2dec(x)


def mod(A, B):
    (q, r) = divide(A, B)
    return r