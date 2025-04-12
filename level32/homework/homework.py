# 2
numbers = [2, 4, 6, 8, 10]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) 

# 3
names = ["Alice", "Bob", "Charlie"]
greetings = list(map(lambda name: "Hello, " + name, names))
print(greetings)  

# 4
fruits = ["apple", "banana", "kiwi"]
lengths = list(map(lambda fruit: len(fruit), fruits))
print(lengths)  

# 5
numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  

# 6
words = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda word: word.startswith('p'), words))
print(p_words)  

# 7
numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)  
#map ფუნქცია იყენებს თითოეული ელემენტის შეცვლას სიაში და აბრუნებს ახალ სიას ხოლო filter ფუნქცია ირჩევს მხოლოდ გარკვეულ პირობებს აკმაყოფილებელ ელემენტებს და აბრუნებს შერჩეულ სიას.
