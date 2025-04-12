#upper uppercases the letters
str = "apple"
upper_str = str.upper()
print(upper_str)


#lower loweracases the letters
str = "apple"
lower_str = str.lower()
print(lower_str)


#capitalize capitalizes the letters
str = "apple"
capitalized_str = str.capitalize()
print(capitalized_str)


#swapcase swapcases the letters
str = "apple"
swapcased_str = str.swapcase()
print(swapcased_str)


#find finds the specified value if not it returns -1
text = "Hello, world!"
index = text.find("world")
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")



#len returns the length of the list
my_list = [10, 20, 30, 40, 50]
length = len(my_list)
print(f"Length of the list: {length}")


#finds the occurance of specified value in the list
fruits = ["apple", "banana", "cherry"]
try:
    banana_index = fruits.index("banana")
    print(f"Banana found at index {banana_index}")
except ValueError:
    print("Banana not found")


#append adds an element to the list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]



#insert inserts an element in the list
colors = ["red", "green", "blue"]
colors.insert(1, "yellow")
print(colors)  # Output: ["red", "yellow", "green", "blue"]


#pop removes and returns the last element in the list
animals = ["cat", "dog", "elephant"]
removed_animal = animals.pop()
print(f"Removed animal: {removed_animal}")
print(animals)  # Output: ["cat", "dog"]



#remove removes the first occurrence of a specified value from a list.
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry", "banana"]


