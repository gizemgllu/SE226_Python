#PART a
dictionary={}

for n in range(1,31):
    value=n*(n-1)
    dictionary[n]=value

print(dictionary)
print("-------------")

#PART b

for key,value in dictionary.items():
    print(str(key) + ":" + str(value))

print("-------------")
#PART c
sum=0
for key,value in dictionary.items():
    sum+=value

print("Summation: "+str(sum))
print("-------------")

#PART d
print("Please enter a number: ")
key=input()

if key.isdigit():
    key = int(key)
    if key in dictionary:
        dictionary.pop(key)
        print("Updated dictionary:", dictionary)
    else:
        print("The entered number is not a key in the dictionary.")
else:
    print("Invalid input. Please enter a number.")

print("--------------")
