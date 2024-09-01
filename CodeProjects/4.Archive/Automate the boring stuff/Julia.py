def countdown(num):
    if num <= 0:
        print("Blastoff!")
    else:
        print(num)
        countdown(num-1)

def countup(num):
    if num > 0:
        print("Blastoff!")
    else:
        print(num)
        countup(num+1)

addNum = int(input("Enter a number: "))
countdown(addNum)
