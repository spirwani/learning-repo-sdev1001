my_square = int(input("Enter number of the sum of squares: "))
square = 1
sum = 0
while square <=my_square:
    square_sum = square*square
    sum = square_sum
    square = square+1
print(f"the sum is: {sum}")
