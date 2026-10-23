def squares(number):
    number = number*number
my_square = int(input("Enter number of the sum of squares: "))
square = 1

while square <=my_square:
   squares(square)
sum = squares(square)
print(f"the sum is: {sum}")
