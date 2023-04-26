def commonElement(l1,l2):

    return list(set(list1)&set(list2))

list1 = [123, 2, 32, 4, 5,76]
list2 = [4, 5, 6, 7, 85]
commons =commonElement(list1, list2)
print(commons)