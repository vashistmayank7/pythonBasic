n = int(input())
str = input()
str_split = str.split(' ')
print(str_split)
for element in str_split:
    print(element)


str2_split = [int(x) for x in input().split()]
print(str2_split)
