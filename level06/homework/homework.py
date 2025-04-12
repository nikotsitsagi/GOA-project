#2) გააკეთეთ account'ის შექმნის მაგალითი, შემოატანინეთ მომხმარებელს სახელი, გვარი, ასაკი, gmail და ამ ყველაფრით გამოიტანეთ classworkში გაკეთებული დავალებისნაირი წინადადება ეკრანზე.
name = input("enter your name: ")
lastname = input("enter yout last name: ")
gmail = input("enter your gmail: ")


print(f"your name is: {name}. your lastname is: {lastname}. your gmail is: {gmail}. ")




#3) მომხმარებელს შემოატანინეთ 3 რიცხვი და მათზე მოახდინეთ მათემატიკური ოპერაციები (+,-,*,/)
number1 = int(input("select your first number: "))
number2 = int(input("select your second number: "))
number3 = int(input("select your third number: "))

print(number1 + number2 + number3)
print(number1 * number2 * number3)
print(number1 / number2 / number3)
print(number1 - number2 - number3)




#4) შექმენით ცვლადი რომელშიც შეინახავთ ნივთის ფასს. მეორე ცვლადში შეინახეთ ნივთების რაოდენობა. თქვენი დავალებაა, რომ დაბეჭდოთ, თუ რამდენი უნდა გადაიხადოთ ნივთების ყიდვისას (ფასი * რაოდენობა)
amount = int(input("enter the amount of product you are buying: "))
price = 30
total_price = amount*price


print(f"your total price is: {total_price}")
