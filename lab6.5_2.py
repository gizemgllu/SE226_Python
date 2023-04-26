def palindrome(strings):

    palindromesList = []
    for x in strings:

        x = "".join(x.split())
        x = x.lower()
        if x == x[::-1]:
            palindromesList.append(x)
    return palindromesList

strings = ["gizem", "AbcbA", "ssdd","kucuk"]
result = palindrome(strings)
print(result)