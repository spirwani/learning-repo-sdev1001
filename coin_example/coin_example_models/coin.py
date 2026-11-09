import random

class Coin:
    VALID_COINS: dict[str, float] = {
        "nickle": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
        "loonie": 1.00,
        "toonie": 2.00   
    }

    def __init__(self, coin_type:str) -> None:
        lowercase_coin_type = coin_type.lower()

        if lowercase_coin_type not in self.VALID_COINS:
            valid_options = ", ".join(self.VALID_COINS.keys())
            raise ValueError(f"invalid coin type: {coin_type}. Must be one of these: {valid_options}") 
        
        self.coin_type: str = lowercase_coin_type
        self.value: float = self.VALID_COINS[lowercase_coin_type]

    def __eq__(self, other: "Coin") -> Bool:
        return self.coin_type == other.coin_type

    def random_flip(self) ->str:
        return random.choice(["heads", "tails"])
    
    
