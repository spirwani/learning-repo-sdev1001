package = input('Insert package: ')
hours = 0
try:
    match package:
        case 'A':
            hours = int(input('Insert number of hours: '))
            if hours >10:
                extra_hours = hours - 10
                total_cost = 9.95 + extra_hours*2
                print(total_cost)
        case 'B':
            hours = int(input('Insert number of hours: '))
            if hours >20:
                extra_hours = hours-20
                total_cost = 13.95+ extra_hours*1
                print(total_cost)
        case 'C':
            hours = int(input('Insert number of hours: '))
            print('$19.95')          
except Exception:
    print('please input a package capital letter')