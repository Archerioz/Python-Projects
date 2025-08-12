secret = 7
guess = 3

if guess > secret:
    print("too high!")
elif guess == secret:
    print("just right :)")
else:
    print("too low!")


small = False
green = True

if small:
    if green:
        print("It's a pea plant!")
    else:
        print("Oh, it's just a raisin.")
elif green:
    print("It's a Watermelon")
else:
    print("It's a huge Pumpkin!")