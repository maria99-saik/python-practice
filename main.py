def subtract_two_lists(list1, list2):
    result_list = []
    for i in range(len(list1)):
        result_list.append(list1[i] - list2[i])
    return result_list
print(subtract_two_lists([8, 9, 7], [1, 2, 3]))
