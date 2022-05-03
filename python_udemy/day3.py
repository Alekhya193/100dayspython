# tresure island

print("welcome to tressure island")
print('Youre at a crossroad. Where do you want to go? Type "left" or "right"')
lr=input()
if(lr=="left"):
    print('Youve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    sw=input()
    if(sw=="wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door=input()

        if(door=="yellow"):
            print("You found the treasure! You Win!")
        elif(door=="red"):
            print("Game over : their was fire")
        elif(door=="blue"):
            print("game over: their were blue tiger")
    else:
        print("Game over: you choose to swim and their was shark")
else:
    print("game over: right was the hole")
