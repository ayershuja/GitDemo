print("hello w")

# here are the comments i have defined

a = 3
print(a)

str = "Hello World"
print(str)

b, c, d = 4, 5.5, "Hello Ayer"
print(b,c,d)

#combine with multiple data type in python
print("{} {} {}".format("Value is",b,c))

# know what type of datatype it is
print(type(d))

greeting ="Welcome to Python programming,"
print(greeting)

instructorName = "Rahul!"
print(greeting,instructorName)


#Data Type :List , we use square bracket and we can delete and update the list

values = [1, 2 , "Ayer Shuja",4.4,5]

print(values[0])
print(values[2])
# To see range from 1 index to 3-1 so answer will be 2 and ayer shuja
print(values[1:3])

# if we want to insert any string in between of list

values.insert(3, "Hina Ayer")
print(values)

# if we want to add anything in last we use append

values.append("shuja hussain")
print(values)

# update the value in index
values[2] = "AYER SHUJA"
print(values)

# delete value in index we use del

del values[2]
print(values)


# Data Type :Tuple , Same as List but tuple we cannot update and delete it, its locked when we use tuple, use round bracket
val= (1, 2, "Ayer", 3, 4,4)
print(val[2])

# Data Type :Dictionary , it uses value not indexes like tuple and list

dic = {"a":2, b:"Ayer", 4:"shuja"}
print(dic[b])
print(dic["a"])

# adding value in dict
dict= {}

dict["firstname"] = "ayer"
dict["lastname"] = "shuja"
dict["c"] = 123

print(dict)


#if condition

greeting = "Good Morning"

if greeting == "Morning":
    print("Condition Matches")
else:
    print("Condition doesnot match")

#Loop : For

obj=[2,3,4,5,9]
for i in obj:
    print(i)

# sum of first natural number 1+2+3+4+5

summation= 0
for j in range(1,6):
    summation = summation+j
print(summation)

# if we want to iterate for every 2 or 3 so we give in range after

for k in range(1,10,2):
    print(k)

# Loop : While
it = 4

while it>1:
    print(it)
    it=it-1
