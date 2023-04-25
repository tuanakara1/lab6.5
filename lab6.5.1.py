def common_elements(list1, list2):

    return list(set(list1) & set(list2))

list1 = [2, 3, 4, 5,8,10]
list2 = [3, 4, 5, 6, 7,8]
print(common_elements(list1, list2))
