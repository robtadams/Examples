# Some pseudo? Maybe?

import random

def primality3(N, k):
    temp2 = mod(N, 2)
    temp3 = mod(N, 3)
    temp5 = mod(N, 5)
    temp7 = mod(N, 7)
    if (temp2 != 0 or temp3 != 0 or temp5 != 0 or temp7 != 0)
        return primality2(N , k)
    print("No")
    return 0

def primality2(N, k):
    for i in range(1, k):
        rand = random.randint(2, N - 1)
        a = exponent(rand, N - 1)
        fermat = mod(a, N)
        if (fermat != 1):
            print("No")
            return 0
    print(N, " is prime")
    return 1