import random

print('Game rules:\n ' 
      + "rock vs paper-> paper win \n"
      + "rock vs scissors-> rock win \n"
      + "paper vs scissors-> scissors win \n"
      )

while True:
    print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissors")
    choice = int(input("Enter your choice:"))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid choice:"))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    
    print("Your choice is \n", choice_name)
    print("Now computer's turn")

    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer's choice is \n", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        print("It's a draw")
        result = 'Draw'
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("Paper wins=>", end=' ')
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Rock wins=>", end=' ')
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        print("Scissors win=>", end=' ')
        result = 'Scissors'

    if result == 'Draw':
        print("It's a draw")
    elif result == choice_name:
        print("User wins")
    else:
        print("Computer wins")

    print("Do you want to play again? (y/n): ")
    ans = input().lower()
    if ans == "n":
        break
print("Thanks for select me")
        