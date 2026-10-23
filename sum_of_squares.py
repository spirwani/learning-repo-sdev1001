import square_calculator  
my_square = int(input("Enter number of the sum of squares: "))
square = 1
sum=0
while square <=my_square:
    sum = square_calculator.calculate_sum_of_squares(square)
    square = square+1
print(f"the sum is: {sum}")
