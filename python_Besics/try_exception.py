#try exception

try:
    value = int(input("enter a value:"))
    print("the output is:",1/value)
except ValueError:
    print("inavlid value")
except ZeroDivisionError:
    print("please eneter valid digit")
except:
    print("entered wrong value")
    
