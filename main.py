def compare_lists(list1, list2):
    nuw_list = []
    for i in range (len(list1)):
        nuw_list.append(list1[i] == list2[i])
    return nuw_list
print(compare_lists([1, 2, 7], [1, 2, 3]))
