import random

def animal_guessing_game():
    animals = {
        "lion": "I am the king of the jungle.",
        "elephant": "I have a long trunk and big ears.",
        "rabbit": "I am small, furry, and love carrots.",
        "zebra": "I have black and white stripes.",
        "kangaroo": "I carry my baby in a pouch.",
        "owl": "I am nocturnal and can rotate my head.",
        "tiger": "I am a big cat with orange fur and black stripes.",
        "penguin": "I am a bird but cannot fly. I live in cold places."
    }
    animal, hint = random.choice(list(animals.items()))
    print("Welcome to the Animal Guessing Game!")
    print("Hint:", hint)
    attempts = 3

    while attempts > 0:
        guess = input("Which animal am I? ").lower().strip()
        if guess == animal:
            print(f"🎉 Correct! The answer is {animal}.")
            break
        else:
            attempts -= 1
            print(f"❌ Incorrect. Try again! Attempts left: {attempts}")
    else:
        print(f"😢 Game Over! The correct answer was: {animal}.")

if __name__ == "__main__":
    animal_guessing_game()
