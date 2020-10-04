print("Rock...")
print("Paper...")
print("Scissors...")

user_1 = input("Player 1 pick Rock, Paper or Scissors: ").lower()
user_2 = input("Player 2 pick Rock, Paper or Scissors: ").lower()



if user_1 == user_2:
    print("Its a tie")

elif user_1 == 'rock':
    if user_2 == 'scissors':
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")

elif user_1 == 'scissors':
    if user_2 == 'paper':
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")

elif user_1 == 'paper':
    if user_2 == 'rock':
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")
else:
    print("Something went wrong")