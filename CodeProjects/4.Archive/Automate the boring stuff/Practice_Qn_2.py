def collatz(number):
    if number % 2 == 0:  # Use modulo operator to check if number is even
        result = (number // 2)
        print(result)
        return result

    else:  # Use else instead of elif for odd numbers
        result = (3 * number + 1)
        print(result)
        return result
addNum = int(input('Enter the number: '))
while addNum != 1:  # Use a while loop instead of a for loop
    addNum = collatz(addNum)



