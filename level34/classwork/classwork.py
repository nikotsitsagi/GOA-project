#1
def manual_map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result
#2
def manual_filter(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result
#3
