num = int(input("Enter a number:"))

value = False
list = []

if num > 1:
    for i in range(2,num):
        if(num%2 == 0):
            value = True
            break
if value:
    list.append(num)
    print("yes its prime number and stored in list",list)
else:
    print("no its not prime number:",t1)

