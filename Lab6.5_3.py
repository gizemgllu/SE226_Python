def myFunction(numb):

    ifPrime = [1] * len(numb)

    for i in range(2, len(numb)):
        if ifPrime[i]:
            for j in range(i * i, len(numb), i):
                ifPrime[j] = 0

    primes = [numb[i] for i in range(2, len(numb)) if ifPrime[i]]

    return primes
