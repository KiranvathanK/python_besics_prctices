#dictinory
print("the dictinory exaples:")

dic = {"tiger":"national_animal","peacock":"national_bird","lotus":"national_flower"}
numbers = {"tiger":1,"Peacock":2,"lotus":3}

print("the dictinory and its numbers:",dic,"\n",numbers,"\n")


#dictinory with for loop with using keys() function

dic = {"tiger":"national_animal","peacock":"national_bird","lotus":"national_flower"}

for key in dic.keys():
    print(key,"=====>",dic[key],"\n")


#example with items() function
dic = {"tiger":"national_animal","peacock":"national_bird","lotus":"national_flower"}

for name,description in dic.items():
    print(name,"====>",description,"\n")


#example with values()  function

dic = {"tiger":"national_animal","peacock":"national_bird","lotus":"national_flower"}

for name in dic.values():
    print("names are:",name)


