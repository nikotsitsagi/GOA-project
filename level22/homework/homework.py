def manual_max(my_list):
    max_value = my_list[0]
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value

def manual_replace(my_list, old_value, new_value):
    for i in range(len(my_list)):
        if my_list[i] == old_value:
            my_list[i] = new_value
    return my_list

def manual_append(my_list, new_value):
    my_list[len(my_list):] = [new_value]
    return my_list
