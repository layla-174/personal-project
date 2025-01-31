print("You wake up with your head pounding, yet no light provides an explanation for why. Your memory doesn't help either - last thing you remember you were sitting in your room. Now you're sitting...well you don't really know where.")
print("WHAT DO YOU DO?")
print("inspect your surroundings OR keep sitting")

answer = input()
with open ("surroundings.txt" , 'r') as file:
    surroundings = file.readlines()

with open ("sitting1.txt" , 'r') as file:
    sitting = file.readlines()

answer = input()
if answer in surroundings:
    print:("You look blah blah blah")
elif answer in sitting:
    print("You stay sitting")
else:
    print("That doesn't sound right...try again")