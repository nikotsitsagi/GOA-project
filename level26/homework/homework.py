mouse = {
    "brand": "Logitech",
    "model": "3",
    "dpi": 4000,
    "buttons": 7,
    "wireless": True
}
computer = {
    "brand": "lenovo",
    "model": "thinkpad",
    "processor": "i7",
    "ram": "16GB",
    "storage": "1TB SSD"
}
keyboard = {
    "brand": "genius",
    "model": "2",
    "switch_type": "Mechanical",
    "backlit": True,
    "connection": "USB"
}
for key in mouse.keys():
    print(key)

for key in computer.keys():
    print(key)

for key in keyboard.keys():
    print(key)

#2)
for value in mouse.values():
    print(value)

for value in computer.values():
    print(value)

for value in keyboard.values():
    print(value)

#3)
for value in mouse.values():
    print(value)

for value in computer.values():
    print(value)

for value in keyboard.values():
    print(value)

#4)
phone = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "color": "Phantom Black"
}

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}

book = {
    "title": "1984",
    "author": "George Orwell",
    "pages": 328
}

fruit = {
    "name": "Apple",
    "color": "Red",
    "taste": "Sweet"
}

city = {
    "name": "Tbilisi",
    "country": "Georgia",
    "population": 1100000
}

#5)
print("The brand of this phone is " + phone["brand"] + " and the model is " + phone["model"])
print("This car is a " + car["year"] + " " + car["brand"] + " " + car["model"])
print("The book titled '" + book["title"] + "' is written by " + book["author"] + " and has " + str(book["pages"]) + " pages")
print("The fruit is an " + fruit["name"] + ", it's " + fruit["color"] + " and tastes " + fruit["taste"])
print("The city of " + city["name"] + " is in " + city["country"] + " with a population of " + str(city["population"]))
