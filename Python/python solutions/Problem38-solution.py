file_name = input("please input file name: ")
file = open(file_name,'r')
lines = file.readlines()
print("Number of lines is " + str(len(lines)))
file.close()
file = open(file_name,'r')
data = file.read()
print(data)
print("Number of characters is "+str(len(data)))
words = data.split()
print("Number of words is "+str(len(words)))
file.close()