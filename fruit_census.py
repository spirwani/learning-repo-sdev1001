fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

print("Voters:")
for voter in fav_fruit_voters.keys():
    print(F"- {voter}")

for vote in fav_fruit_voters.values():
    if vote == "banana":
        voting_results["banana"] += 1
    elif vote == "apple":
        voting_results["apple"] += 1
    elif vote == "orange":
        voting_results["orange"] += 1

print("Voting Results:")
print(voting_results)


total_votes = 0
for count in voting_results.values():
    total_votes += count
print(f"Total votes cast: {total_votes}")