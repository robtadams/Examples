# main.py
# Robert Adams
# Andre Judson

import base
import solutions

def main():
    print ("1) (A^B) - (C^D)")
    print ("2) (A^B) / (C^D)")
    print ("3) 1 + 1/2 + 1/3 + ... + 1/A")
    print ("4) A + B")
    print ("5) TwosComp")
    print ("6) A / B")
    print ("7) Exit")

    print("Input: ", end='')
    user = input()

    while user != 4:

        if user == '1':
            print("A:", end='')
            a = input()
            print("B:", end='')
            b = input()
            print("C:", end='')
            c = input()
            print("D:", end='')
            d = input()
            print(solutions.problem1(int(a),int(b),int(c),int(d)))

        if user == '2':
            print("A:", end='')
            a = input()
            print("B:", end='')
            b = input()
            print("C:", end='')
            c = input()
            print("D:", end='')
            d = input()
            (q, r, num, den) = solutions.problem2(int(a),int(b),int(c),int(d))

            print(base.bin2dec(num), "/", base.bin2dec(den))
            print("Quotient: ", q)
            print("Remainder: ", r)

        if user == '3':
            print("A:", end='')
            a = input()
            (num, den) = solutions.problem3(int(a))
            N1 = base.bin2dec(num)
            D1 = base.bin2dec(den)
            print(N1, "/", D1)


        if user == '4':
            print("A: ", end='')
            a = int(input())
            print("B: ", end='')
            b = int(input())

            A1 = base.dec2bin(a)
            print("A Bin: ", A1)
            A2 = base.bin2dec(A1)
            print("A Dec: ", A2)

            B1 = base.dec2bin(b)
            print("B Bin: ", B1)
            B2 = base.bin2dec(B1)
            print("B Dec: ", B2)

            ret = base.Add(a, b)
            print ("A + B (dec): ", ret)
            print ("A + B (bin): ", base.dec2bin(ret))


        if user == '5':
            print("A: ", end='')
            a = input()
            A = base.dec2bin(int(a))
            TwosA = base.TwosComp(A)
            print(base.bin2dec(TwosA))

        if user == '6':
            print ("A: ", end='')
            a = input()
            print ("B: ", end='')
            b = input()
            (q, r) = base.Divide(int(a), int(b))
            print("Quotient: ", base.bin2dec(q))
            print("Remainder: ", base.bin2dec(r))

        if user == '7':
            return 0

        print("Input: ", end='')
        user = input()


main()




