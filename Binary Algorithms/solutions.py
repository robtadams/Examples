# solutions.py
# Robert Adams
# Andre Judson

import base

def problem1(A, B, C, D):
    P1 = Exponent(A, B)
    P2 = Exponent(C, D)
    print(base.bin2dec(P1), "-", base.bin2dec(P2))

    Answer = sub(P1, P2)

    return base.bin2dec(Answer)

def problem2(A, B, C, D):
    P1 = Exponent(A, B)
    P2 = Exponent(C, D)

    (q, r) = base.Divide(base.bin2dec(P1), base.bin2dec(P2))

    Q = base.bin2dec(q)
    R = base.bin2dec(r)

    return (Q, R, P1, P2)


#1  + 1/2 + 1/3 + ... + 1/N
def problem3(A):
    if A == 1:
        return ([1, 0],[1, 0])

    num = [1, 0]
    den = [1, 0]

    for X in range(2, A + 1):
        #print("X: ", X)
        (num, den) = fraction_add(num, den, [1, 0], base.dec2bin(X))

    temp_num = base.bin2dec(num)
    temp_den = base.bin2dec(den)

    #g = base.dec2bin(gcd(temp_num, temp_den))
    g = gcd(temp_num, temp_den)
    print("Num: ", temp_num)
    print("Den: ", temp_den)
    print("GCD: ", g)

    if g != 1:
        (num, rNum) = base.Divide(temp_num, g)
        (den, rDen) = base.Divide(temp_den, g)

    return (num, den)

def fraction_add(P,Q,R,S):
    #print("P: ", P, "Q: ", Q, "R: ", R, "S: ", S)
    mult1 = base.mult(P, S)
    mult2 = base.mult(Q, R)

    num = base.add(mult1, mult2)
    den = base.mult(Q, S)

    #print("Mult1: ", base.bin2dec(mult1))
    #print("Mult2: ", base.bin2dec(mult2))
    #print("Num: ", base.bin2dec(num))
    #print("Den: ", base.bin2dec(den))

    return (num, den)

def sub(A, B):
    tempA = A[:]
    tempB = B[:]
    return base.add(tempA, base.TwosComp(tempB))

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
       return (base.mult(val,val))
   else:
       temp = sub(B, [1,0])
       temp.pop(0)
       val = exponent(A, temp)
       return base.mult(base.mult(val,val),A)


def Exponent(A, B):
    ret = exponent(base.dec2bin(A), base.dec2bin(B))
    ret.append(0)
    return ret


def gcd(A, B):
    if B > A:
        temp = A
        A = B
        B = temp
    if (A % B) == 0:
        return B

    return gcd(B, A%B)