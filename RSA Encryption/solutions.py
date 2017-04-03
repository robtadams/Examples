# solutions.py
# Robert Adams
# Andre Judson

import random
import base

debug = False
count = 0

def encryption(m, n, k):

    global debug

    m = int(m)
    n = int(n)
    k = int(k)

    (N, E, D) = key_gen(n, k)

    temp_m = base.Mod(m, N)

    if debug is True:
        print()
        print("-----Beginning Encryption-----")
        print()
        print("Original Message: ", m)
        print("Modulo Message: ", temp_m)
        print("N: ", N)
        print("E: ", E)
        print("D: ", D)
        print()

    en_m = encrypt(N, E, temp_m)

    if debug is True:
        print()
        print("===MESSAGE ENCRYPTED===")
        print()
    de_m = decrypt(N, D, en_m)

    if debug is True:
        print("===MESSAGE DECRYPTED===")
        print()
        print("Your original message was", m)
        print()

    print("Your encrypted message is", en_m)
    print("Your decrypted message is", de_m)
    print("Your modded message is   ", temp_m)

    return 1


def encrypt(N, E, M):

    global debug

    N = int(N)
    E = int(E)
    M = int(M)

    if debug is True:
        print("--- ENCRYPTION ---")
        print()
        print("N:", N)
        print("E:", E)
        print("M:", M)
        print()

    # C = M**E % N
    c = base.Mod_Exp_Log(M, E, N)

    if debug is True:
        print(M, "**", E, "%", N, "=", c)
        print()

    return c


def decrypt(N, D, M):

    global debug

    N = int(N)
    D = int(D)
    M = int(M)

    if debug is True:
        print("--- DECRYPTION ---")
        print()
        print("N:", N)
        print("D:", D)
        print("M:", M)
        print()

    # C = M**D % N
    c = base.Mod_Exp_Log(M, D, N)
    if debug is True:
        print(M, "**", D, "%", N, "=", c)
        print()

    return c


def key_gen(n, k):

    global debug

    rand1 = gen_prime(n, k)
    rand2 = gen_prime(n, k)

    while rand1 <= 1:
        rand1 = gen_prime(n, k)

    while rand2 <= 1:
        rand2 = gen_prime(n, k)

    if debug is True:
        print("Your first random prime number is: ", rand1)
        print("Your second random prime number is: ", rand2)

    # N = p x q
    # E = gcd(E, (p-1)(q-1)) = 1
    # D = DE ≡ 1 (mod N)

    temp1 = rand1 - 1
    temp2 = rand2 - 1
    totient = base.Mult(temp1, temp2)

    N = base.Mult(rand1, rand2)
    E = gcd_1(totient, len(base.dec2bin(totient)))

    while base.gcd(E, N) != 1:
        if debug is True:
            print("GCD(", E, ",", N, ") != 1; Recalculating E")
        E = gcd_1(totient, len(base.dec2bin(totient)))

    (d, D) = euclid_ext(E, totient)
    D = int(D)
    d = int(d)

    test = (d * E) % totient

    while d < 0 or test != 1:
        if debug is True:
            print("=== d IS LESS THAN ZERO; RECALCULATING d ===")
        E = gcd_1(totient, len(base.dec2bin(totient)))

        while base.gcd(E, N) != 1:
            if debug is True:
                print("GCD(", E, ",", N, ") != 1; Recalculating E")
            E = gcd_1(totient, len(base.dec2bin(totient)))

        (d, D) = euclid_ext(E, totient)
        D = int(D)
        d = int(d)

        test = (d * E) % totient

    if debug is True:
        print("Your first random prime number is: ", rand1)
        print("Your second random prime number is: ", rand2)

    return N, E, d


# GE ≡ 1 (mod N)
# Will only work if GCD(E, N) == 1
def euclid_ext(E, N):

    global debug

    E = int(E)
    N = int(N)

    if N > E:
        if debug is True:
            print(N, ">", E, "; Switching values for euclid_ext()")
        temp_N = N
        temp_E = E
        N = temp_E
        E = temp_N


    global count
    count += 1

    if debug is True:
        print(count, ". euclid_ext(", E, ",", N, ")")

    if N == 0:
        return (0, 0)

    temp = base.Mod(E, N)

    # print("Making recursive call to euclid_ext(", N, ",", temp, ")")

    # print("--- Making recursive call: euclid_ext(", N, ",", temp, ")")
    (euclid, old_euclid) = euclid_ext(N, temp)

    if debug is True:
        print()
        print("---Computing Extended Euclid's Theorem---")
        print("E: ", E)
        print("N: ", N)
        print("euclid: ", euclid)
        print()

    temp1 = E * euclid
    if debug is True:
        print(E, "*", euclid, "=", temp1)
    temp2 = 1 - temp1
    if debug is True:
        print("1 - (", E, "*", euclid, ") =", temp2)
    temp3 = temp2 // N
    if debug is True:
        print("(1 - (", E, "*", euclid, "))/", N, "=", temp3)
        print()
        print("(", E, "*", euclid, ") + (", N, "*", temp3, ") = 1")
    temp4 = E * euclid
    temp5 = N * temp3
    if debug is True:
        print(temp4, "+", temp5, "=", temp4 + temp5)
        print()

    return temp3, euclid


def gcd_1(N, bits):

    global debug

    rand = random.getrandbits(bits)

    while rand == 0:
        rand = random.getrandbits(bits)

    while base.gcd(N, rand) != 1:
        rand = random.getrandbits(bits)

    return rand


def gen_prime(N, K):

    global debug

    i = 0

    N = int(N)
    temp = random.getrandbits(N)
    rand = base.dec2bin(temp)

    if len(rand) > 1:
        if rand[0] != 1:
            rand[0] = 1
    if len(rand) > 2:
        if rand[-2] != 1:
            rand[-2] = 1

    while True:

        i += 1

        val = base.bin2dec(rand)

        while val < 0:
            rand = base.dec2bin(temp)

            if len(rand) > 1:
                if rand[0] != 1:
                    rand[0] = 1
            if len(rand) > 2:
                if rand[-2] != 1:
                    rand[-2] = 1

            val = base.bin2dec(rand)

        if debug is True:
            print("Testing val: ", val)
        prime = Primality3(val, K)

        if prime == 1:
            if debug is True:
                print("Gen_Prime took ", i, " operations to complete!")
            return val

        temp = random.getrandbits(N)
        rand = base.dec2bin(temp)

        while temp < 2:
            temp = random.getrandbits(N)
            rand = base.dec2bin(temp)

        if rand[0] != 1:
            rand[0] = 1
        if rand[-2] != 1:
            rand[-2] = 1


def Primality3(N, k):
    n = base.dec2bin(int(N))
    return primality3(n, int(k))


def primality3(N, k):

    global debug

    test2 = base.mod(N, [0,1,0])
    test3 = base.mod(N, [1,1,0])
    test5 = base.mod(N, [1,0,1,0])
    test7 = base.mod(N, [1,1,1,0])

    temp2 = base.bin2dec(test2)
    temp3 = base.bin2dec(test3)
    temp5 = base.bin2dec(test5)
    temp7 = base.bin2dec(test7)

    if temp2 != 0 and temp3 != 0 and temp5 != 0 and temp7 != 0 and base.bin2dec(N) > 1:
        if debug is True:
            print("Passed Primality3; Testing Primality2")
        return primality2(N , int(k))
    return 0


def primality2(N, k):

    global debug

    N.append(0)
    temp = base.bin2dec(N)
    for i in range(0, k):
        if temp - 1 < 2:
            temp = 3
        rand = random.randint(2, temp - 1)
        fermat = base.Mod_Exp_Log(rand, temp - 1, temp)

        if fermat != 1:
            if debug is True:
                print("Failed after", i + 1, "operation(s)")
                print()
            return 0
        else:
            if debug is True:
                print("Passed test", i + 1, "out of", k)

    return 1
