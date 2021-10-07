import random

def absolute_function(x):
    if x<0 :
        return x * -1
    else:
        return x


def guess():
    x = (random.randint(1,10))
    r = int(input(("Please guess my number:")))
    k = x - r
    if k == 0:
        print(" You got it right!")
    else:
        print("Sorry, my number was " + str(x) + ". You were " + str(absolute_function(k)) + " away from it.")


guess()