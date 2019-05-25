# 1. a = 2 suppose a_main = 2 created with some reference and in increment(a) a_increment = 2 created but when a = a +2 now a_increment
# is new variable and we are returning same reference here that is why out put in print will be 2
# in case 2 we are storing the new reference and printing the new reference hence output will be 4 in this case

def increment(a):
    a = a + 2
 # case 1   return
    return a

a = 2
# Case 1 increment(a)
# case 2
a = increment(a)
print(a)