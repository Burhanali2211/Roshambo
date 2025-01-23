import random

# Define the rules with emojis
rules = ["Rock 🪨", "Paper 📄", "Scissor ✂️"]

# Ask for the user's name
name = input("Welcome! What's your name? ")

# File to save the results
results_file = "roshambo_results.txt"

# Function to display the menu
def menu():
    print("\nHello, {}! Welcome to the Roshambo Game!".format(name))
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissor ✂️")
    print("Enter 0 to Exit.")

# Game loop
with open(results_file, "w") as file:
    file.write(f"Game Results for {name}:\n")
    file.write("=" * 30 + "\n")

menu()

while True:
    try:
        # Computer's choice
        computer = random.choice(rules)

        # User's input
        user = int(input("\nEnter Your Choice (1/2/3 or 0 to Exit): "))

        # Exit condition
        if user == 0:
            print("Thank you for playing, {}! Results saved to {}.".format(name, results_file))
            break

        # Validate the user's choice
        if user in [1, 2, 3]:
            user_choice = rules[user - 1]

            # Display choices
            print(f"\nYour choice: {user_choice}")
            print(f"Computer's choice: {computer}")

            # Determine the result
            if user_choice == computer:
                result = "It's a tie! 🤝"
            elif (user_choice == "Rock 🪨" and computer == "Scissor ✂️") or \
                 (user_choice == "Paper 📄" and computer == "Rock 🪨") or \
                 (user_choice == "Scissor ✂️" and computer == "Paper 📄"):
                result = "You win! 🎉"
            else:
                result = "Computer wins! 😢"

            # Print the result
            print(result)

            # Save the result to the file
            with open(results_file, "a") as file:
                file.write(f"Your choice: {user_choice}\n")
                file.write(f"Computer's choice: {computer}\n")
                file.write(f"Result: {result}\n")
                file.write("-" * 30 + "\n")
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

    except ValueError:
        print("Please Enter a Valid Input (1, 2, 3, or 0 to Exit)!")
