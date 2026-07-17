
import random
print("! ! ! Welcome to the Number guesser Game ! ! !\nGuess the number from 1 to 100\n")
system = random.randint(1,100)
difficulty = input("Choose your Difficulty Level\nEASY / MEDIUM / HARD\n").lower()
if difficulty == "easy":
    attempts = 12
elif difficulty == "medium":
    attempts = 8
elif difficulty == "hard":
    attempts = 4
else:
    print("Invalid Difficulty!\nTry again")
    
while attempts > 0:
    print(f"You have {attempts} attempts remaining")
    user = int(input("Guess the number : "))
    
    if user > system:
        print("Go lower")
        attempts -= 1
    elif user < system:
        print("Go Higher")
        attempts -= 1
    else:
        print("you Guessed it!\nYou Won!")
        break
    
if attempts == 0:
    print(f"You lost your attempts\nThe number is {system} ")