#Syntax Error: როდესაც პროგრამის კოდი არ აკონფორმირდება დოკუმენტაციის წესების მიხედვით.
#TypeError არის Python-ის შეცდომა, რომელიც წარმოიქმნება არასწორი ტიპის მონაცემების გამოყენებისას.
#NameError წარმოიქმნება მაშინ, როდესაც Python-ში ცვლადი ან ფუნქცია უცნობია.
#IndexError წარმოიქმნება, როდესაც სიის ან მასივის მიუწვდომელ ინდექსზე ვცდილობთ წვდომას.
#ValueError წარმოიქმნება მაშინ, როდესაც ფუნქცია ან მეთოდი მიიღებს არასწორ ტიპის არგუმენტს.

try:
    print(variable)
except NameError:
    print("The variable is not defined.")



my_list = []

try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")


try:
    number = int("abc")
except ValueError:
    print("Cant convert the string to an integer.")


try:
    # ვცდილობთ ტექსტის გადაქცევას მთელ რიცხვად (int)
    number = int("abc")
except ValueError:
    # თუ ValueError წარმოიქმნება, გადავიდეთ ამ ბლოკში
    print("Cant convert the string to an integer.")
