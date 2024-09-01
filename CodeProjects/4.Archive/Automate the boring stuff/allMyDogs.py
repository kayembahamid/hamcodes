DogNames = []
while True:
    print("Enter the name of Dog" + str(len(DogNames) + 1) + " 1(Or enter nothing to stop.):")

    name = input()
    if name == "":
        break
    DogNames = DogNames + [name] # list concatenation
print("The Dog names are:")
for name in DogNames:
    print(" " + name)
