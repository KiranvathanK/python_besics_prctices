#The provided code stub reads and integer,n , from STDIN.
#For all non-negative integers i<n, print i^2.
total = 0
n = int(input("enter a number:"))

for i in range(n+1):
    total = i ** 2
print(total)
