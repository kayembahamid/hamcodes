def spam():
    eggs = 'spam local'
    print(eggs)  # this prints the local spam string

def bacon():
    eggs = 'bacon local'
    print(eggs) # this prints the bacon local
    spam()
    print(eggs) # print local varaible  bacon local

eggs = 'global'
bacon()
print(eggs) # this print out global
