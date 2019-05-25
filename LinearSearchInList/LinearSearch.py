print('Please enter the number separated by space')
li = [int(x) for x in input().split()]
print('Please enter the number to search')
number = int(input())
isNumberFound = False
for i in range(len(li)):
    if number == li[i]:
        isNumberFound = True
        print('Index is----------> ',i)
        break
if isNumberFound is False:
    print(-1)
