# To read and write from text file

file=open('test.txt')

#Read all the content of file
#Read n number of character by passing parameter
#print(file.read(5))

# to read single line by line, so output will be 1 and 2nd line
#print(file.readline())
#print(file.readline())




# print line by line using readLine Method
'''
line=file.readline()
while line !="":
    print(line)
    line=file.readline()
'''

for line in file.readlines():
    print(line)


file.close()