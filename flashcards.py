# Create an empty dictionary
# come up with 5 vocabulary words as a group. It can be related to python or something separate
# Create a dictionary with the vocabulary words as keys and a nested dictionary with the definition and key 
import random

my_dictionary = {
    "kangaroo": {"the pocket mammal that carries around its joey": "kangaroo"},
    "red panda": {"the center of much internet adoration, a mammal with a striped tail and the cutest of faces": "red panda"},
    "alpaca": {"the alpine llama, it bounces around and occasionally sounds a loud honk": "alpaca"},
    "lemur": {"the mammal with the largest of eyes, that stares longingly at the piece of fruit in your hand": "lemur"},
    "praying mantis": {"the insect that slices the air with its green blades, warding off friend and foe": "praying mantis"}
}

# Make a list out of the values and pick a random question
my_list = []
answer_list = []
for key in my_dictionary:
    answer_list.append(key)
    for key in my_dictionary[key]:
        my_list.append([key])
x = random.randint(0, len(my_list) - 1)
print(x)        
print("What is", my_list[x], "?")

# Use the built in input() function to get user input for the answer
answer = input()

# Compare the input to the key and print correct if its right, and incorrect if its wrong. 
if answer == answer_list[x]:
    print("Correct")
else:
    print("Wrong")

# Wrap this all in a function called flash_cards(dictionary)
def flash_cards(dictionary):
    my_list = []
    answer_list = []
    for key in dictionary:
        answer_list.append(key)
        for key in dictionary[key]:
            my_list.append([key])
    x = random.randint(0, len(my_list) - 1)
    print(x)        
    print("What is", my_list[x], "?")
    answer = input()
    if answer == answer_list[x]:
        print("Correct")
    else:
        print("Wrong")
