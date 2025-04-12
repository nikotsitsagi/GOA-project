#1) შექმენით if else condition რომელიც მომხმარებელს გაუკეთებს ფასდაკლებას თუ ის 18 წელზე ნაკლებისაა
age = int(input("enter your age here: "))

if age < 18:
      age == True
      print("discount")
else:
      print("regular price")

#2) გააკეთეთ ლატარეა, თუ მომხმარებელს ამოუვა რიცხვი 6 დაუპრინტეთ რომ მოიგო სახლი, თუ ამოუვა რიცხვი 30 დაუპრინტეთ რომ მოიგო ჰავაის ბილეთი, სხვა შემთხვევაში დაუპრინტეთ რომ მოიგო 1 დოლარი
number = int(input("hello you are participating in a lottery choose a number to win a house, ticket to hawaii and 1 dollar. choose your number here: "))
if number == 30:
      number = True
      print("Congratulations! you just won a trip ticket to hawaii. ")
elif number == 6:print("Congratulations! you just won a house. ") 


else: print("Congratulations! you just won 1 dollar. ")


#3) შექმენით if else condition  რომელიც მომხმარებელს გაუკეთებს ფასდაკლებას თუ ის 18 წელზე ნაკლებისაა ან სტუდენტია
is_student = input("Hello are you a sudent?: ")
age = int(input("enter your age here: "))
if age < 18 and is_student:
      age = True
      is_student = False
      print("discount")
else:
      print("regular price")





