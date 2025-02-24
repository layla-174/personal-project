
print("Welcome to 'ESCAPE'. The aim of the game is in the title - you must escape. You will be given choices that will determine whether or not you succeed in escaping. In some circumstances you will be given a 'FATE OR LUCK' question, where a random choice will also determine the outcome. Type 'play' to begin.")
answer = input()
play = ["play", "start playing", "PLAY"]

if answer in play:
    print("You wake up with your head pounding, yet no light provides an explanation for why. Your memory doesn't help either - last thing you remember you were sitting in your room. Now you're sitting...well you don't really know where.")
    print("WHAT DO YOU DO?")
    print("inspect your surroundings OR stay sitting")

    with open ('surroundings.txt' , 'r') as file:
        surroundings = file.readlines()
    with open ('sitting.txt' , 'r') as file:
        sitting = file.readlines()
    with open ('room1.txt', 'r') as file:
        library = file.readlines()
    with open ('room2.txt', 'r') as file:
        cellar = file.readlines()
    with open ('room3.txt', 'r') as file:
        bedroom = file.readlines()

        answer = input()
        if answer+"\n" in surroundings:
            print("You try to look around but there's one problem...you can't see anything. After stumbling for a while you feel something resembling a flashlight, but of course - just your luck - it has no batteries.")
            print("WHAT DO YOU DO?")
            print("try to find batteries OR look for a different light source")
            answer = input()
            
            with open ('batteries.txt', 'r') as file:
                batteries = file.readlines()
            with open ('lightsource.txt', 'r') as file:
                lightsource = file.readlines()
            with open ('lighton.txt', 'r') as file:
                lighton = file.readlines()
  
            if answer+"\n" in batteries:
                print("You decide to look for the batteries of the flashlight, which in hindsight seems pretty futile. Just as you're about to give up, two metal cylinders almost miraculously make their way into your hand. As you turn on the flashlight, you finally see where you are.")
                print("FATE OR LUCK?")
                print("choose a whole number between 1-3")
                answer = input()
                if answer+"\n" in library:
                    print("library")
                elif answer+"\n" in cellar:
                    print("cellar")
                elif answer+"\n" in bedroom:
                    print("You were in your room the whole time. Oops.")
                else:
                    print("idk")
    
            elif answer+"\n" in lightsource:
                print("You discard the useless flashlight, and continue to rely on your other senses to find a source of light. Due to the darkness, you bump into a wall, and - despite your initial irritation - the feeling of what seems to be a light switch subdues your anger. Though, you hesitate, thinling it's a trap. You have a gut feeling telling you to go with the safer option.")
                print("WHAT DO YOU DO?")
                print("turn on the light OR go back to the flashlight")
                answer = input()
                if answer+"\n" in lighton:
                    print("lights on")
                elif answer+"\n" in batteries:
                    print("You decide to look for the batteries of the flashlight, which in hindsight seems pretty futile. Just as you're about to give up, two metal cylinders almost miraculously make their way into your hand. As you turn on the flashlight, you finally see where you are.")
                    print("FATE OR LUCK?")
                    print("choose a whole number between 1-3")
                    answer = input()
                else:
                    print("idk")
        elif answer+"\n" in sitting:
            print("You stay sitting")
        else:
            print("That doesn't sound right...try again")
            print("WHAT DO YOU DO?")
            print("inspect your surroundings or stay sitting")

else:
    print("I don't quite understand")
