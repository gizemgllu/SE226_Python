from math import factorial


n = input("Enter the value of n: ")
x = input("Enter the value of x: ")


if not (n.isdigit() and x.isdigit()):
    print("Invalid input!")
else:
    n = int(n)
    x = int(x)

    func = lambda n, x: (n ** x) / factorial(x) if x >= 0 else 0


    total = [1] + [func(n, i) for i in range(1, x + 1)]
    result = sum(total)

    print("The result: ", result)
