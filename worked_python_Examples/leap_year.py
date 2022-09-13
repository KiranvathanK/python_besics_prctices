#Leap year

year = int(input("enter a valid year:-"))

if(year%400 == 0) and (year%100 == 0):
    print("Its leap year")
    
elif(year%4 == 0) and (year%100!= 0):
    print("Its leap year")
else:
    print("Its not a leap year")
