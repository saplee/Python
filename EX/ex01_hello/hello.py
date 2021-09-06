"""EX01 hello."""
# ask for a name.
name = input("What is your name?")
# ask for first random number.
num1 = int(input(f"Hello, {name}! Enter a random number:"))
# ask for second random number.
num2 = int(input("Great! Now enter a second random number:"))
sum1 = num1 + num2
# print out sum.
print(f"{num1} + {num2} is {sum1}")
"""Poem"""
# asks some color.
some_color = input("Enter some color")
# asks some plural noun.
noun = input("Enter some plural noun")
# asks some verb.
verb = input("Enter some verb")
# print out poem.
print(f"""Roses are {some_color},
{noun} are blue, I love to {verb},
And so will you!""")
"""Greeting"""
# asks greeting word.
str1 = input("Enter a greeting: ")
# asks a recipient.
greeting = input("Enter a recipient: ")
# asks how many times to repeat.
num = int(input("How many times to repeat:"))
# print out greeting + recipient many times you wrote
print((str1 + " " + greeting + "! ") * num)
