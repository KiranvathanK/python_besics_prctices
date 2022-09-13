
#1.Task
#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5 , print Not Weird
#If n is even and in the inclusive range of 6 to20 , print Weird
#If n is even and greater than 20 , print Not Weird

n = int(input("Enter a number:"))
if n%2!= 0:
    print("wired")
elif n >= 2 and n <= 5:
    print("not wired")
elif n >= 6 and n <= 20:
    print("wired")
elif n > 20:
    print("not wired")
else:
    print("invalid entry")

    
