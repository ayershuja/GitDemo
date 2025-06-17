str= "AyerShujaAcademy.com"
str1="Consulting Firm"
str3 = "AyersShuja"
str4 = "              Great             "

print(str[1])

print(str[0:4]) # if you want to do substring in python

print(str[0:4]+str1)  #concatentaion of two strings

print(str3 in str) # validating if string is present in main string

var=str.split(".") # spliting the string with any data , we use that in bracket
print(var)
print(var[0])

print(str4.strip()) # trim
print(str4.lstrip()) # trim left
print(str4.rstrip()) # trim right
