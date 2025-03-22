import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def is_game_over(self):
        return self.current_round >= self.total_rounds

    def play_round(self):
        self.current_round += 1
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in self.choices:
            user_choice = input("Invalid choice! Enter rock, paper, or scissors: ").lower()
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = self.find_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
        else:
            print("Computer wins this round!")

    def play_game(self):
        while not self.is_game_over():
            self.play_round()
        print("\nGame Over!")
        print(f"Final score - You: {self.user_wins}, Computer: {self.computer_wins}")
        if self.user_wins > self.computer_wins:
            print("Congratulations, you won the game!")
        elif self.user_wins < self.computer_wins:
            print("Computer wins the game! Better luck next time.")
        else:
            print("It's a tie game!")

rounds = int(input("Enter the number of rounds: "))
game = Rock_paper_scissors(rounds)
game.play_game()
