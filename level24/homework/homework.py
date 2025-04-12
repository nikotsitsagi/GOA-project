#list
my_list = [1, 2, 3, 4]
print(my_list[0])

my_list.append(5)
print(my_list)

my_list[1] = 'a'
print(my_list)

my_list.insert(2, 'b')
print(my_list)


#tuple
my_tuple = (1, 2, 3)
print(my_tuple[0])

print(my_tuple.count(2)) 

print(my_tuple.index(3))

new_tuple = my_tuple + (4, 5)
print(new_tuple)

print(2 in my_tuple)

for item in my_tuple:
    print(item)

    length = len(my_tuple)
print(length)

mixed_tuple = (1, "string", 3.14, True)
print(mixed_tuple)

#sets
my_list = [1, 2, 3, 4]
element = my_list[0]

my_list.append(5)

my_list[1] = 'a'

my_list.remove(3)

my_list.insert(2, 'b')

new_list = [6, 7, 8]
my_list.extend(new_list)

my_list.reverse()

length = len(my_list)

#ტუპლები შეიქმნა იმისათვის რომ მონაცემთა ბაზა შეენახათ, ლისტები შეიქმნა ელემენტების შესანახად რომლებიც მარტივი მისაწვდომია, სეტები შეიქმნა უნიკალური ელემენტების შესანახად, მათზე ოპერაციების გასაკეთებლად.






