zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:
   f.write('\n' + ' and '.join(zoo)) # On a new line in  "output.txt", add all elements from the zoo list, joined by " and "
   f.write('\n' + str(number)) # Add the number to the output as well


