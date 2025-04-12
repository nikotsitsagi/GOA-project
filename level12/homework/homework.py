#2)
number = 1
while number <= 100:
    if 50 <= number <= 60:
        number = number + 1
        continue
    print(number)
    number = number + 1 

#3)
num = 1
total = 0
while total <= 50:
    print(num)
    total = total + num
    if total == 50:
        break
    num = num + 1



#4) 
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("ლუწი.")
else:
    print("კენტი.")


#5)
# მომხმარებლისგან რიცხვის მიღება
score = int(input("enter a number: "))


if 90 <= score <= 100:
    grade = "Grade A"
elif 80 <= score < 90:
    grade = "Grade B"
elif 70 <= score < 80:
    grade = "Grade C"
elif 60 <= score < 70:
    grade = "Grade D"
elif 0 <= score < 60:
    grade = "Grade F"
else:
    grade = "wrong number"



#6)
age = int(input("enter your age: "))


if age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
else:
    print("You are a grown up")



print(grade)

