#example1
list = [1,2,3,4,5]

print(list,"\n")

#example2
list2 = [20,30,40,50,60]
list2[2] = 33

print("updated list:",list2,"\n")

#example3
list3 = [12,13,14,15,16,17]
del list3[1]
print("after deleted list:",list3,"\n")


#example4
list4 = [1,2,3,4,5]
list4.append(12)
print("the added value",list4,"\n")

#example5
list5 = [100,200,201,203,204]
list5.insert(1,202)
print("new inserted list",list5,"\n")

#example6
number = [121,122,123,124,125]
print("the values by using negative idices:",number[-3])
