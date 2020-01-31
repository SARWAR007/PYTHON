fh = open("Names.txt","r")  # open the file
#print(fh.read())# read the file
print(fh.readline())
print(fh.readline())
print(fh.readlines())

print(fh.read())


fh.close()#close the file

