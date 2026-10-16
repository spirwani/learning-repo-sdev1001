try:
    cost = float(input("Enter pizza cost: $"))
    people = int(input("Enter number of people: "))
    if cost >0 and people >0:
        print(f"Each person owes ${cost/people:.2f}")
    else:
        print('Please input a positive number')
except:
    print("Please input an int value for both inputs.")

    