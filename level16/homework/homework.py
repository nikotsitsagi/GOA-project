#1)
def number_generator(start, end):
    result = []
    for num in range(start, end + 1):
     result.append(num)
    return result
start_num = int(input("enter your starting number: "))
end_num = int(input("choose your ending number: "))
number_list = number_generator(start_num, end_num)
print("here are your numbers:", number_list)
#2)
#name
def name():
 name = input("enter your name: ")
 return f"my name is {name}"
print(name())
def surname():
 surname = input("enter your surname: ")
 return f"my name is {surname}"
print(surname())
def studyplace():
 studyplace = input("enter the place where you study: ")
 return f"i study in {studyplace}"
print(studyplace())
#3)
def greeting_by_name_surname():
    return f"hello {name + " " + surname3}"
name = input("enter your name here: ")
surname3 = input("enter your surname: ")
print(greeting_by_name_surname())
#4)
def sum_of_two_numbers(a, b):
    return a + b
result = sum_of_two_numbers(3, 5)
print("result:", result)
#5)
def multiply_three_numbers(a, b, c):
    return a * b * c
result = multiply_three_numbers(2, 3, 4)
print("result:", result)
#6)
def list_foods(food_list):
    for food in food_list:
        print(food)
my_foods = ["xachapuri", "xinkali", "mwvadi", "tolma"]
list_foods(my_foods)







   