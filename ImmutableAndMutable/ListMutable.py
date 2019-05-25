li = [2,4,77,23,13]
li2 = li
# mutable as we are able to change the value
li2[2] = 78
print(li)
print(li2) 
print('id of li is ----> ',id(li), 'id of li2 is ---------> ', id(li2))
li2 = [4,5]
print(id(li))
print(id(li2))