print("Please enter your name,lab grade, midterm grade and final grade: ")
name=input()


lab=input()


mid=input()


final=input()


lastScore= float(lab)*0.25+ float(mid)*0.35+float(final)*0.4
print("Name: "+name)
print("Lab: "+lab)
print("Midterm: "+mid)
print("Final: "+final)
print("Last Score: "+str(lastScore))
