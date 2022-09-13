#by using function validate given input bcm triangle r not

def is_triangle(a,b,c):
    return a+b>c and b+c>a and c+a>b

a = float(input("enter a 1st value:"))
b = float(input("enter a 2nd value:"))
c = float(input("enter a 3rd value:"))

if is_triangle(a,b,c):
    print("ues its Triangle")
else:
    print("oh no its not Triangle")
