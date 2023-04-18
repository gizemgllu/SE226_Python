
result = 0

def function(n):
    """
    Calculates the sum: ∑(-1)^(k+1)/k; k=1, n
    Parameters:
        int n
    Returns:
        None
    """
    global result

    if n == 0:
     exit
    else:

        x = (-1) ** (n + 1) / n
        result += x
        function(n - 1)

n = int(input("Please enter n: "))


function(n)


print("The result: ", result)
