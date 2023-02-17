'''Set comprehensions
Comprehension in python provide us with a short and compact way to create new sequences (in case of set it's set comprehensions).'''

# set comprehension 
# for creating new set 

Set = [1, 2, 3, 4, 5, 6, 7] 

Set_comp = {var for var in Set if var % 2 == 0} 

print("New Set using set comprehensions:",Set_comp)


'''Zip() function
The zip function returns a zip object contains a paired iterator, which is an iterator of tuples. In this pair it basically pair first element from two tuples and so on.'''

a = ("Rick", "Mary", "Sonia")
b = ("Raj", "Susan", "Jenn") 

x = zip(a, b) 
#convert zip object into tuple so that it can be iterable 
print(tuple(x)) 
