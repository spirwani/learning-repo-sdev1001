print("Average age of student calculator")
age_total = 0
while_counter = 0
try:
    while True:
        age = input('Enter age of student or stop')
        if age == 'stop':
            break
        else:
            age_total = int(age)+age_total
            while_counter = while_counter+1
            break
    age_average = age_total/while_counter
except:
    print('No ages to average')
else:
    print(f'Average age is: {age_average}')

