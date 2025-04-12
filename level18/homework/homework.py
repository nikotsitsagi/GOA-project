#2)
a = 5
b = 7
total = a + b
print("Sum of a and b:", total)
#3)
version1 = "Python"
version2 = "Java"
combined_version = version1 + " and " + version2
print("Combined version:", combined_version)
#კონკატენაცია არის სტრინგების შეერთება

#4)
a = 10
b = 3
result = a / b
print("result (float):", result)
#პითონი ავტომატურად ითვლის და არჩევს რომელი ტიპის ცვლადია
#5)
# >
print(10 > 5)


# <
print(15 < 30)


# !=
print(6 != 1)



# ==
print(5 == 5)



# <=
print(921 <= 921)



# >=
print(1234 >= 1245)
#6)
a = 5
b = 3

# 1. ==
print(a == b)  # False

# 2. !=
print(a != b)  # True

# 3. <
print(a < b)   # False

# 4. >
print(a > b)   # True

# 5. <=
print(a <= b)  # False

# 6. >=
print(a >= b)  # True

# 7. and
print(a < 10 and b > 2)  # True

# 8. or
print(a < 10 or b > 5)   # True
#8)
x = 10
y = 7
print(x != y)  # Output: True

x = 5
y = 5
print(x == y)  # Output: True

a = True
b = False
result = a or b
print(result)  # Output: True

a = True
b = False
result = a and b
print(result)  # Output: False

a = 5
b = 3
print(a < b)   # output: False
#9)
for i in range(1 , 11):
    print(i)
#10)
total = 0
for num in range(1, 10):
    total = total + num

print(total)
#11)
text = "Hello, World!"
for l in text:
    print(l)
#12)
number = 1
while number <= 10:
    print(number)
    number += 1
#13)
number = 1
while number <= 100:
    if 50 <= number <= 60:
        number += 1
        continue
    print(number)
    number += 1
#14)
total = 0
number = 1
while total < 50:
    total += number
    number += 1
print("Sum of numbers:", total)
#15)
def divides(number):
    if number % 3 == 0 or number % 5 == 0:
        print(f"{number} is dividable by 3 or 5")
    else:
        print(f"{number} is not dividable by 3 or 5")

user_input = int(input("Enter a number: "))
divides(user_input)
#16)
def average_of_list(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return None
    return total / count

test_list = [1, 3, 4, 5, 2]
result = average_of_list(test_list)
print("Average:", result)
#17) #?
#18)
def square_of_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

input_list = [1, 3, 4, 5, 2]
output_list = square_of_numbers(input_list)
print("Squared numbers:", output_list)
#19)
#upper 
str = "apple"
upper_str = str.upper()
print(upper_str)


#lower 
str = "apple"
lower_str = str.lower()
print(lower_str)


#capitalize 
str = "apple"
capitalized_str = str.capitalize()
print(capitalized_str)


#swapcase
str = "apple"
swapcased_str = str.swapcase()
print(swapcased_str)


#find 
text = "Hello, world!"
index = text.find("world")
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")



#len 
my_list = [10, 20, 30, 40, 50]
length = len(my_list)
print(f"Length of the list: {length}")


#.index
fruits = ["apple", "banana", "cherry"]
try:
    banana_index = fruits.index("banana")
    print(f"Banana found at index {banana_index}")
except ValueError:
    print("Banana not found")


#append 
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  



#insert 
colors = ["red", "green", "blue"]
colors.insert(1, "yellow")
print(colors)  


#pop 
animals = ["cat", "dog", "elephant"]
removed_animal = animals.pop()
print(f"Removed animal: {removed_animal}")
print(animals)  



#remove
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  





