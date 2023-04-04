#PART a

divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {}
united_we_stand.update(divided)
united_we_stand.update(we_fall)

print("Name    Age")
for key,value in united_we_stand.items():
    print(f"{key:<8}{value}")

print("----------")

#PART b

united_we_stand.pop('Nat')
print(united_we_stand)

print("-----------")

#PART c

newSorted=sorted(united_we_stand.items())
print(newSorted)

print("-----------")

#PART d

maxValue = max(united_we_stand.values())
minValue = min(united_we_stand.values())
print("Maximum value:", maxValue, "and Minimum value:", minValue)