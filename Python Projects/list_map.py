def find_greater(list_all):

    #desired_no = list_all[1]
    for index in list_all:

        if (index > 6):

            print(index)

    return index






list1 = [1,6,8,40,5,3,7]

number = 6

find_greater(list1)

print(list(filter(find_greater,[1,6,8,40,5,3,7])))
