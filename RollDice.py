import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        again = input("Roll again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Dice Simulator!")
            break

if __name__ == "__main__":
    main()
