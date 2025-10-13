#Roger Blake
#A program that generates a random number and the user has to guess it.
import random

def game(name):
    random_number = random.randint(1, 20)
    guesses = 0

    print(f"Hello {name}, I have selected a number between 1 and 20 for you to guess. You have 6 tries to get it correct.")

    while guesses < 6:
        guess = int(input("what is your guess? "))
        guesses += 1

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations {name}! You Guessed the number in {guesses} tries!")
            return
        
    print(f"Sorry {name}, you have run out of tries. The secret number was {random_number}.")
        
def main():
    
    print("Welcome to -Guess the number- game!")
    name = input("what is your name? ")

    while True:
        game(name)
        play_again = input("Would you like to play again? Yes or No: ").lower()
        if play_again != "yes":
            print(f"Thank you for playing my game {name}, goodbye!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
        