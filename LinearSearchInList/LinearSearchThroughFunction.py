def linearSearch(li, number):
    isNumberFound = False
    for i in range(len(li)):
        if number == li[i]:
            isNumberFound = True
            return i
            break
    if isNumberFound is False:
        return -1

n = int(input())
listValue = [int(x) for x in input().split()]
result = linearSearch(listValue,n)
print('Index is ----------> ',result)
