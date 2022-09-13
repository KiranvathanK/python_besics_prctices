def message():
    print("good morning")


message() #function calling hear
print("good afternoon")
print("good night\n")

#------------------------------------------
#parameter function
#example1
#------------------------------------------

def add(a,b):
    print("the sum of a and b is:",a+b,"\n")

add(23,44)

#example2
#------------------------------------------
def sum_list(list):
    total = 0
    for i in list:
        total+= i
    print("the sum of list is:",total,"\n")

sum_list([1,2,3,4,5,6,7,8])

#------------------------------------------
#positional parameter function
#example
#------------------------------------------
def positional(fname,lname):
    print("my name is:",fname,lname,"\n")

positional("kiran","k")

#------------------------------------------
#keyword parameter function
#example
#------------------------------------------
def keyword(name,age,gender,phn):
    print("details","name is",name,"ages is:",age,"gender is:",gender,"phone number is:",phn,"\n")

keyword(name="kiran_k",age=25,gender="male",phn=9999999999)

#function and return
#example
def function():
    return 1234

x = function()
print(x)
































    



