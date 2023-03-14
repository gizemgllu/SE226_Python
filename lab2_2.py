print("Please enter a number between 3 and 9(inclusive): ")
s = int(input())

if s >= 3 and s <= 9:
    for i in range(s):
        print("*" * (i+1))

    for i in range(s-1):
        print("*" * (s-i-1))
else:
    print("Please enter a valid value!")



