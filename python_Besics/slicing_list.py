#slicing

list = [123,122,34,45,67,89]
x = list[:]

print("the list values:",x,"\n")

#slicing with some values

list = [121,22,3,45.6,34,True]
var = list[0:4]

print("updated list",var,"\n")

#slicing with negetive indices

list = [1,22,33,56,78,98]
new_list = list[0:-3]

print("new list is:",new_list,"\n")

#slicing

new_list = [3,4,6,8,9,34,45]
list = new_list[:-1]

print("the list is",list)
