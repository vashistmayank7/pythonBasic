a = 5
b = 3
# printing the reference of b here before changing the value
print(id(3))
# Changing the value of b by assiging value of a
b = a
b = 5
# In python variables are immutable we change the reference but cannot change the value
print(a)
print(b)
print(id(a))
print(id(b))