print("Welcome to 'THE ROOM.' To play, type 'play'. To save progress, type 'save'")
answer = input()
play = ["play", "start playing"]
save = ["save", "save progress"]

if answer in play:
    print("You wake up with your head pounding, yet no light provides an explanation for why. Your memory doesn't help either - last thing you remember you were sitting in your room. Now you're sitting...well you don't really know where.")
    print("WHAT DO YOU DO?")
    print("inspect your surroundings OR stay sitting")

    with open ('surroundings.txt' , 'r') as file:
        surroundings = file.readlines()

    with open ('sitting.txt' , 'r') as file:
        sitting = file.readlines()

        answer = input()
        if answer+"\n" in surroundings:
            print("You look blah blah blah")
        elif answer+"\n" in sitting:
            print("You stay sitting")
        elif answer in save:
            print("Your progress has been saved.")
        else:
            print("That doesn't sound right...try again")
            print("WHAT DO YOU DO?")
            print("inspect your surroundings or stay sitting")

elif answer in save:
            print("Your progress has been saved.")
else:
    print("That doesn't sound right...try again")
    print("Welcome to 'THE ROOM.' To play, type 'play'. To save progress, type 'save'")