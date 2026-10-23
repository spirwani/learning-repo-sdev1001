import random

def guess_items_price(guess):
    guess = int(input("guess the price: "))
    price = random.randint(1,10)
    price1 = random.randint(1,10)
    price2 = random.randint(1,10)
    prices = [price, price1, price2]
    
    if guess == prices[0] or guess == prices[1] or guess == prices[2]:
        return'winner'
    else:
        return'loser'
    