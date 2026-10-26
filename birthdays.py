#birthday dictioary
birthday = {
    "Dan": "april 14th",
    "Gary": "june 23rd",
    "Richard": "february 2nd",
    "Jessica": "october 30th",
    "Mary": "december 25th"
}

name = input("Who's birthday do you want to look up?")
if name in birthday:
    print(f"{name}'s birthday is {birthday[name]}")
else:
    print(f"We don't have {name}'s birthday")