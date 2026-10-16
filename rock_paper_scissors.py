import random
choice = int(input('Rock(0), Paper(1), Scissors(2)'))
match choice:
    case 0:
        print('You chose rock')
    case 1:
        print('You chose paper')
    case 2:
        print('you chose scissors')
    case _:
        print('pick 0, 1 ,2')
robot_choice = random(0,2)
match robot_choice:
    case 0:
        print('robot chose rock')
    case 1:
        print('robot chose paper')
    case 2:
        print('robot chose scissors')
    
    case _:
        print('did not pick a option')

if choice == robot_choice:
    print('Tie')
elif (choice == 0 and robot_choice == 2) or (choice == 1 and robot_choice == 0) or(choice == 2 and robot_choice == 1):
    print('player wins')
elif (robot_choice == 0 and choice == 2) or (robot_choice == 1 and choice == 0) or (robot_choice==2 and choice == 1):
    print('robot wins') 