def split_lines(line):

    data = line

    print(data)
    n = len(data)-1
    #print("length is",n)
    s =n/3
    print("Partition is:",s)

    avg = len(data) / float(s)
    print("Partition is:",avg)
    print(type(avg))

    list1=[]

    x = 0.0

    count = 0

    i =0
    
    while x < n:

        

        list1.append(data[int(x):int(x+avg)])

        x += avg

    print(list1)
      
    for items in range(len(list1)):

        count += 1

        print("List:",list1[0])
        print("List:",list1[1])
        print("List:",list1[2])

        str1 = list1[0]

        String1 = str(str1)

        print("String is :", String1)

        str2 = list1[1]

        String2 = str(str2)

        str3 = list1[2]

        String3 =str(str3)


file_name = open('Names.txt','r')

fh = file_name.read()

lines = fh.strip("\n")
#print("Lines are :",lines)

line_1 = lines.split()

print("Contents are:",line_1)

split_lines(line_1)
