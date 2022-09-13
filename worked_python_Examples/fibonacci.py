def fib(n):
    if n<1:
        return none
    if n<3:
        return 1
    ele1=ele2=1
    the_sum=0
    
    for i in range(3,n+1):
        the_sum=ele1+ele2
        ele1,ele2 = ele2,the_sum
    return the_sum


for n in range(1,8):
    print(n,"->",fib(n))
