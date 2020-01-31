from functools import reduce
def product(list_all):

    list2 = []

    for index  in range(len(list_all)-1):

        print("Index",index)
        print("Index +1 ",index+1)
        list_all_2 = list_all[index] * list_all[index+1]
        list2.append(list_all_2 * list_all[index+1])
    return list2

list1 = [1,2,3,4]

print(product(list1))

print(reduce(lambda a,b:a*b,[1,2,3,4]))
