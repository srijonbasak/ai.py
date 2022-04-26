count = 0
print("Wellcome to My Computer Game")
command = input("Do you want to start ? ")
if command.lower() != "yes":
    quit()
ans1 = int(input("What is 2+2"))
if ans1 != 4:
    print("You dump its 4")
else:
    print("Correct!")
    count += 1
ans1 = int(input("What is 49-1"))
if ans1 != 48:
    print("You dump its 48")
else:
    print("Correct!")
    count += 1
ans1 = int(input("What is 2+6"))
if ans1 != 8:
    print("You dump its 4")
else:
    print("Correct!")
    count += 1
print(f"{count} ans is correct")
