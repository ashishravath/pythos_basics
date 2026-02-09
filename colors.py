#creating a tuple of four colors and try to change one
colors = ('red', 'green', 'blue', 'yellow')
#colors[0] = 'orange' #this will give an error because tuples are immutable
#to change a value in a tuple, we can convert it to a list, change the value, and then convert it back to a tuple
colors_list = list(colors) #convert tuple to list
colors_list[0] = 'orange' #change the value in the list
colors = tuple(colors_list) #convert list back to tuple
print(colors) #this will print the updated tuple with 'orange' instead of 'red'
