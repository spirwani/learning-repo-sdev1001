shows = ['Silicon Valley', 'Halt and Catch Fire', 'Blackberry', 'The Billion Dollar Code', 'Mr. Robot', 'The IT Crowd', 'WeCrashed', 'The Social Network', 'Severance', 'Pirates of Silicon Valley']
print(f'first item: {shows[0]}')
print(f'last item: {shows[-1]}')
shows[6] = 'the dropout'
shows[7] = 'black mirror'
print(f'the 5th to 9th shows are: {shows[4:9]}')
print('the top 5 shows are: ')
index = 0
while index <5:
    print(shows[index])
    index = index+1