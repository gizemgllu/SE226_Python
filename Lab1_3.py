
name = input("Enter student name: ")
lab = float(input("Enter lab grade : "))
mid = float(input("Enter midterm grade : "))
final = float(input("Enter final grade : "))

lastScore = (lab * 0.25) + (mid * 0.35) + (final * 0.4)


print("Name: "+name )
print("Lab: "+str(lab))
print("Midterm: "+str(mid))
print("Final: "+str(final))
print("Last Score: "+str(lastScore))
