import random
price = random.randint(1,10)
price1 = random.randint(1,10)
price2 = random.randint(1,10)
prices = [price, price1, price2]
guess = int(input("guess the price: "))
if guess == prices[0] or guess == prices[1] or guess == prices[2]:
    print('winner')
else:
    print('loser')
print(f'the prices were{prices}')
    
