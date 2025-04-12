#2)  მომხმარებელს შემოატანინეთ 2 რიცხვი და შეადარეთ ერთმანეთს ყველანაირად (6ივე შედარების ოპერატორით რაც გავიარეთ)
number_1 = input("enter your first number here: ")
number_2 = input("enter your second number here: ")
print(f"here are your number comparisons:")
print(f"1)(>) if you compared {number_1} > {number_2}, your comparison is {number_1 > number_2}")
print(f"2)(<) if you compared {number_1} < {number_2}, your comparison is {number_1 < number_2}.")
print(f"3)(==) if you compared {number_1} == {number_2}, your comparison is {number_1 == number_2}.") 
print(f"4)(!=) if you compared {number_1} != {number_2}, your comparison is {number_1 != number_2}.")
print(f"5)(<=) if you compared {number_1} <= {number_2}, your comparison is {number_1 <= number_2}.")
print(f"6)(>=) if you compared {number_1} >= {number_2}, your comparison is {number_1 >= number_2}.")



#3) გატესტეთ ყველა შედარების ოპერატორი რაც დღეს ვისწავლეთ (ყველაზე გააკეთ 3-3 მაგალითი) ეს კლასშიც გავაკეთეთ მაგრამ ახლა სანამ გაუშვებთ დაუწერეთ გვერდზე კომენტარები თუ რას გამოიტანს
# >
print(78 > 5) #True
print(700> 214) #True
print(1214> 4455) #False

# <
print(15 < 30) #True
print(90 < 169) #True
print(156 < 39) #False

# !=
print(2 != 2) #False
print(3298 != 1204) #True
print(890 != 890) #False


# ==
print(12 == 12) #True
print(1300 == 100) #False
print(560 == 214) #False


# <=
print(525 <= 525) #True
print(300 <= 120) #False
print(400 <= 550) #True


# >=
print(9000 >= 4245) #True
print(1200 >= 600) #True
print(500 >= 1200) #False



#4)გამოიყენეთ ერთი ცვლადის სახელი და reassign. შექმენით რაიმე ცვლადი და შეადარეთ რაიმე რიცხვს, შემდეგ კი შეუცვალეთ მნიშვნელობა ისე რომ წინაზე გამოტანილი მნიშვნელობის საწინააღმდეგო გამოიტანოს. e.g: თუ თავიდან გამოიტანა True ახლა გამოატანინეთ False, თუ თავიდან გამოიტანა False ახლა გამოატანინეთ True
number_1 = input("enter your first number here: ")
number_2 = input("enter your second number here: ")
print(f"here are your number comparisons:")
print(f"1)(>) if you compared {number_1} > {number_2}, your comparison is {number_1 < number_2}")
print(f"2)(<) if you compared {number_1} < {number_2}, your comparison is {number_1 > number_2}.")
print(f"3)(==) if you compared {number_1} == {number_2}, your comparison is {number_1 != number_2}.") 
print(f"4)(!=) if you compared {number_1} != {number_2}, your comparison is {number_1 == number_2}.")
print(f"5)(<=) if you compared {number_1} <= {number_2}, your comparison is {number_1 >= number_2}.")
print(f"6)(>=) if you compared {number_1} >= {number_2}, your comparison is {number_1 <= number_2}.")