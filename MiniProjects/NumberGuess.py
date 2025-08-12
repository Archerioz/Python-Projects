#Only lets you guess once for right now, I'll recreate it with a while loop soon.
print()
print("---NUMBER GUESSING GAME PROTOTYPE---")
print()

print("Welcome to the number guessing game, a game where you only have ONE chance to guess the number!")
print("Pass your device to another person for them to write down the single digit secret number from 1-10!")
print()

secret_num = input("What Would you like to set the secret number to?: ")
print()

player = input("So player, what's your name?: ")
print("I see, nice to meet you", player + ". Now let's begin!")
print()
print()

guess = input(player + ", What will your guess be? Think carefully since you've got a single chance!: ")
print()
    
if guess > secret_num:
    print("You lost! You guessed too high")
elif guess < secret_num:
    print("You lost! You guessed too low")
else:
    print("Phenomenal job! You guessed to number exactly!")