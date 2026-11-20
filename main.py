def get_max_elements(list1, list2):
    new_list = []
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            new_list.append(list1[i])
        else:
            new_list.append(list2[i])
    return new_list
print(get_max_elements([1, 10, 5], [4, 2, 5]))