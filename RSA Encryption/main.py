# main.py
# Robert Adams
# Andre Judson

import base
import solutions

def main():

    print("1) Primality3")
    print("2) Generate a random prime number")
    print("3) Generate encryption keys")
    print("4) Encrypt message")
    print("5) Decimal Mod Exp (Linear)")
    print("6) Decimal Mod Exp (Logarithmic)")
    print("7) Extended Euclid's Algorithm (Will only work if gcd(E,N) == 1)")
    print("8) Encryption/Decryption")
    print("9) Quit")
    print("Input: ", end='')
    user = input()

    while user != 9:

        if user == '1':
            print("Enter an integer to be tested for primality: ", end='')
            N = input()
            print("Enter number of times number is to be tested: ", end='')
            K = input()
            if solutions.Primality3(N, K):
                print("The value", N, "is a prime number.")
            else:
                print("The value", N, "is NOT a prime number.")

        if user == '2':
            print("Enter an integer (greater than 5) for the number of bits: ", end='')
            N = input()
            while int(N) < 5:
                print("Enter an integer (greater than 5) for the number of bits: ", end='')
                N = input()
            print("Enter number of times number is to be tested: ", end='')
            K = input()
            print("Your random prime number is: ", solutions.gen_prime(N, K))

        if user == '3':
            print("Enter an integer (greater than 5) for the number of bits: ", end='')
            N = input()
            while int(N) < 5:
                print("Enter an integer (greater than 5) for the number of bits: ", end='')
                N = input()
            print("Enter number of times number is to be tested: ", end='')
            K = input()

            (N, E, D) = solutions.key_gen(N, K)

            print("N: ", N)
            print("E: ", E)
            print("D: ", D)

        if user == '4':
            print("Enter an integer (greater than 5) for the number of bits: ", end='')
            N = input()
            while int(N) < 5:
                print("Enter an integer (greater than 5) for the number of bits: ", end='')
                N = input()
            print("Enter number of times number is to be tested: ", end='')
            K = input()
            print("Enter a message (this will be modulo N): ", end='')
            M = input()

            solutions.encryption(M, N, K)

        if user == '5':
            print("Enter a Base: ", end='')
            A = input()
            print("Enter a Exponent: ", end='')
            B = input()
            print("Enter a Modulus: ", end='')
            C = input()
            print(A, "**", B, "%", C, " = ", base.Mod_Exp(A, B, C))

        if user == '6':
            print("Enter a Base: ", end='')
            A = input()
            print("Enter a Exponent: ", end='')
            B = input()
            print("Enter a Modulus: ", end='')
            C = input()
            print(A, "**", B, "%", C, " = ", base.Mod_Exp_Log(A, B, C))

        if user == '7':
            print("Enter an integer for E: ", end='')
            E = input()
            print("Enter an integer for N: ", end='')
            N = input()

            print("The output for euclid_ext(", E, ",", N, ") is", solutions.euclid_ext(E, N))

        if user == '8':
            print("Enter a value for N: ", end='')
            N = input()
            print("Enter a value for E: ", end='')
            E = input()
            print("Enter a value for D: ", end='')
            D = input()
            print("Enter a value for M: ", end='')
            M = input()

            N = int(N)
            E = int(E)
            D = int(D)
            M = int(M)

            temp_M = M % N

            en_m = solutions.encrypt(N, E, temp_M)
            de_m = solutions.decrypt(N, D, en_m)

            print("Your original message is", temp_M, "(", M, "%", N, ")")
            print("Your encrypted message is", en_m)
            print("Your decrypted message is", de_m)

        if user == '9':
            print("Quit")
            return

        print("Input: ", end='')
        user = input()

main()




