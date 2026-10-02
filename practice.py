import random

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Calculate the remainder when dividing by 12
zodiac_index = year % 12

# Determine the Chinese Zodiac animal based on the remainder
match zodiac_index:

    case 0:
        print("monkey")
    case 1:
        print("rooster")
    case 2:
        print("dog")
    case 3:
        print("pig")
    case 4:
        print("rat")
    case 5:
        print("ox")
    case 6:
        print("tiger")
    case 7:
        print("rabbit")
    case 8:
        print("dragon")
    case 9:
        print("snake")
    case 10:
        print("horse")
    case 11:
        print("sheep")
    case _:
        print("invalid")

        

user_input =  int(input("Scissor (0), rock (1), paper (2): "))
computer_input = random.randint(0, 2)

user_result = ""
match user_input:
    case 0:
        user_result = "scissor"
    case 1:
        user_result = "rock"
    case 2:
        user_result = "paper"
    case _:
        print("undefined")

if computer_input == 0:
    computer_result = "scissor"
elif computer_input == 1:
    computer_result = "rock"
elif computer_input == 2:
    computer_result = "paper"

# tie
if user_result == computer_result:
    print(F"The computer is {computer_result}. You are {user_result}. It is a draw")
# user wins
elif ((user_result == "paper" and computer_result == "rock") or 
      (user_result == "rock" and computer_result == "scissor") or
      (user_result == "scissor" and computer_result == "paper")):
    print(F"The computer is {computer_result}. You are {user_result}. You win")
# computer wins
elif ((computer_result == "paper" and user_result  == "rock") or 
      (computer_result == "rock" and user_result  == "scissor") or
      (computer_result == "scissor" and user_result  == "paper")):
    print(F"The computer is {computer_result}. You are {user_result}. You lose")

# Clean up the code to make it better
# - the code above can be modified to make cleaner, more efficient, and less prone to typos. How?