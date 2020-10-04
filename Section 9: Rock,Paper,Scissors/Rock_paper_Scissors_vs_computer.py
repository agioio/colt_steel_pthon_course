from random import choice

print("Rock...")
print("Paper...")
print("Scissors...")

plays = ["scissors","rock","paper"]

computer = choice(plays)

user_1 = input("Player pick Rock, Paper or Scissors: ").lower()

print(f'The computer plays: {computer}')

if user_1 == computer:
    print("Its a tie")

elif user_1 == 'rock':
    if computer == 'scissors':
        print("Player 1 wins!!!")
    else:
        print("Computer wins!!!")

elif user_1 == 'scissors':
    if computer == 'paper':
        print("Player 1 wins!!!")
    else:
        print("Computer wins!!!")

elif user_1 == 'paper':
    if computer == 'rock':
        print("Player 1 wins!!!")
    else:
        print("Computer wins!!!")
else:
    print("Something went wrong")