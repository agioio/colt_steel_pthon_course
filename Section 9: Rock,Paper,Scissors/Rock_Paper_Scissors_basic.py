print("Rock...")
print("Paper...")
print("Scissors...")

valid_choices = ["rock","paper","scissors"]

user_1 = ''
while user_1.lower() not in valid_choices:
    user_1 = input("Player 1 pick Rock, Paper or Scissors: ")

user_2 = ''
while user_2.lower() not in valid_choices:
    user_2 = input("Player 2 pick Rock, Paper or Scissors: ")


if user_1.lower() == "rock" and user_2.lower() == 'scissors':
    print("Player 1 is the winner!!!")
elif user_1.lower() == "paper" and user_2.lower() == 'rock':
    print("Player 1 is the winner!!!")
elif user_1.lower() == "scissor" and user_2.lower() == 'paper':
    print("Player 1 is the winner!!!")
elif user_1.lower() == user_2.lower():
    print("It is a draw.")
else:
    print("Player 2 is the winner!!!")