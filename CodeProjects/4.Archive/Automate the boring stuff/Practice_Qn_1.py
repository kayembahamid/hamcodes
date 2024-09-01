#1. What are the two values of the Boolean data type? How do you write them?
True and False
#2. What are the three Boolean operators?
# and , not/andnot , or
#3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
#True and True   True
#True and False  False
#False and False True
#False and True  True
#True or False   True
#True or True    True
#False or False  False
#4. What do the following expressions evaluate to?
#                 (5 > 4) and (3 == 5)         false
#                 not (5 > 4)                  false
#                 (5 > 4) or (3 == 5)          true
#                 not ((5 > 4) or (3 == 5))    false
#                 (True and True) and (True == False) false
#                 (not False) or (not True)    true
#5. What are the six comparison operators?
# == ,=! ,> , >=, < , <=,
#6. What is the difference between the equal to operator and the assign- ment operator?
# == and the assignment is =
#7. Explain what a condition is and where you would use one.
# is a statement which would result to false or true
# we can use in if statement and while loops
#8. Identify the three blocks in this code:
#                 spam = 0
#                 if spam == 10:
#                     print('eggs')  1st
#                     if spam > 5:
#                         print('bacon')  2nd
#                     else:
#                         print('ham')    3rd
#                     print('spam')
#                 print('spam')
#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
#stored in spam, and prints Greetings! if anything else is stored in spam.
spam = 1
print("write 1 or 2  ")
input(int())
if spam == 1:
    print("Howdy")
elif spam == 2:
    print("Greetings")
else:
    print("spam")
#10. What can you press if your program is stuck in an infinite loop?
# exit / break /cntrl c or z
#11. What is the difference between break and continue?
# break stops the loop
#12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
# from 1 to 10 , 1 to 9 ,0 to 10 ,
#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
#14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?