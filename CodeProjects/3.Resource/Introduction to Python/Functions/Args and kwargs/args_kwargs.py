def random_dialogue(place, *args, **kwargs):
    print("-- Do you know how to get to the", place, "?")
    print("-- I'm sorry, I am not from here, no idea about the", place)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
    print('\n')


random_dialogue("Library", "Do you at least have a cigar, sir?",  #call 1
                "Sure, help yourself.",
                lost_person="old banker",
                other_guy="street clown",
                scene="in a park")

dic = {"lost_person": "old banker", "other_guy": "street_clown", "scene": "in a park"}
lst = ["Do you at least have a cigar, sir?", "Sure, help yourself."]
random_dialogue("Library", *lst, **dic)  # Call 2 - the exact same output


def cat(food, *args, state='still hungry', action='meow', breed='Siamese'):
    print(f"-- This cat would {action}", end=' ')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")
    for arg in args:
        print(arg.upper())


# Add a list of phrases that will be capitalized.
phrases = ['It is too fat ', ' You are feeding your cat too much ']
# Add a dict of keyword arguments.
keywords = {'state': 'fat', 'action': 'eat', 'breed': 'Maine coon'}
# Call the cat() function like in example above to print the required output.
cat('anything', *phrases, **keywords) # invoke cat with some food, phrases and keywords
