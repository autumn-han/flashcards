import random

my_dictionary = {
    "kangaroo": {"the pocket mammal that carries around its joey": "kangaroo"},
    "red panda": {"the center of much internet adoration, a mammal with a striped tail and the cutest of faces": "red panda"},
    "alpaca": {"the alpine llama, it bounces around and occasionally sounds a loud honk": "alpaca"},
    "lemur": {"the mammal with the largest of eyes, that stares longingly at the piece of fruit in your hand": "lemur"},
    "praying mantis": {"the insect that slices the air with its green blades, warding off friend and foe": "praying mantis"}
}

def flash_cards(dictionary):
    my_list = []
    answer_list = []
    for key in dictionary:
        answer_list.append(key)
        for key in dictionary[key]:
            my_list.append([key])
    x = random.randint(0, len(my_list) - 1)      
    print("What is", my_list[x], "?")
    answer = input()
    if answer == answer_list[x]:
        print("Correct")
    else:
        print("Wrong")

flash_cards(my_dictionary)