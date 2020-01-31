def squares_list(list_all):

    #list_2 = []

    for index,val in enumerate (list_all):

        #print(list_all[index])

        list_all[index] = list_all[index] * list_all[index]

    return list_all




list1 = [2,3,4,5,6]

print(squares_list(list1))
