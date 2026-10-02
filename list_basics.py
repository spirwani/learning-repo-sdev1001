#indexing starts at 0
colours = ['red', 'blue', 'yellow', 'pink']
print(colours)

number_of_elements = len(colours)
print(number_of_elements)
print(colours[3])
#with slicing, upper boundray is not inclusive
print(colours[0:2])

#you can start and omit last index
print(colours[:3])
print(colours[-1:])

numbers = [7,38,5,29,0]
#Python has the sort method, which sorts in accerlating order by default
numbers.sort()
print(numbers)
# reverse = True to sort desending
numbers.sort(reverse=True)
print(numbers)
#append adds an item to end
#insert(index, value) adds the value to the index
#pop removes the item at index
#remove removes by value(first instance)
#pop returns removed item while remove doesn't
#remove prints an error if it doesn't exist, so check to see if it is


