function1 = lambda x, y: x + y
result = function1(12,5)
print(result)


function2 = lambda x, y: x * y
result = function2(12,2)
print(result)

list_range = lambda start, end: list(range(start, end + 1))
start = 1
end = 15
result= list_range(start,end)
print(result)

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

words = ["hello", "world", "python"] 
capitalized_words = list(map(lambda word: word.capitalize(), words)) 
print(capitalized_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)

numbers = [3, 9, 15, 22, 27, 30]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)





