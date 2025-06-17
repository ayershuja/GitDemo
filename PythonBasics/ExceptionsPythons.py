
itemInCart = 0

# if 2 item were added into cart, if you dont meet the condition

'''
if itemInCart != 2:
    raise Exception("Product cart not matching")

'''

#OR

assert (itemInCart==0)

#try and catch
try:
    with open('test12.txt','r') as reader:
        reader.read()
except:
    print("No file found")

# to know the error what its throwing so we use except with Exception e
try:
        with open('test123.txt', 'r') as reader:
            reader.read()
except Exception as e:
        print(e)

#Finally : it will run either its fail and pass in try and catch block

finally:
    print("Cleaning all resources")