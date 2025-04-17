import random

def play_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("🎲 I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("🤔 Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low!")
            elif guess > number_to_guess:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

def main():
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
