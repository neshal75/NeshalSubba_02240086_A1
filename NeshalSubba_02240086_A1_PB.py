import random

def Game_of_guessing_number():
    number_to_guess = random.randint(1, 100)
    user_attempts = 0
    print("Welcome to the Game")
    print("guess the number between 1 to 100.")
    
    while True:
        try:
            User_guess = int(input("enter your number: "))
            user_attempts += 1
            if User_guess < number_to_guess:
                print(" It low! Retry.")
            elif User_guess > number_to_guess:
                print(" It high buddy, try again you can do it.")
            else:
                print(f" WOW!  You win the Game,  you have guess the correct number {number_to_guess} in {user_attempts} attempts.")
                break
        except ValueError:
            print("  Wrong input! Please enter the number between 1 to 100.")

def rock_paper_scissors():
    select = ['rock', 'paper', 'scissors']
    computer_select = random.choice(select)
    player_select = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if player_select not in select:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    print(f"Computer chose: {computer_select}")
    
    if player_select == computer_select:
        print("It's a draw! Try again ")
    elif (player_select == 'rock' and computer_select == 'scissors') or \
         (player_select == 'paper' and computer_select == 'rock') or \
         (player_select == 'scissors' and computer_select == 'paper'):
        print(" You win! You beat the computer")
    else:
        print("You lose! Computer beat you")

def main():
    while True:
        print("\nMenu")
        print("Select the option(1-3) given below")
        print("1. Guess The Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Exit the System")
        
        select = input(" Select a function (1-3): ")
        
        if select == '1':
            Game_of_guessing_number()
        elif select == '2':
            rock_paper_scissors()
       
        elif select == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()