#1)
numbers = [x for x in range(1, 101)]
print(numbers)


#2)
numbers2 = [x for x in range(1, 101) if x % 2 == 0]
print(numbers2)


#3)
letters = ["niko","giorgi","luka"]
capitalizedletters = [letters.upper() for letters in letters]
print(capitalizedletters)

#4)
numbers3 = [x**2 for x in range(1, 11)]
print(numbers3)

