def reverseList(li):
    length = len(li)
    for i in range (length//2):
        li[i],li[length-1-i] = li[length-1-i], li[i]

li = [2,4,5,12,53,57]
reverseList(li)
print(li)

def reverseList2(li):
    length = len(li)
    for i in range(length//2):
        li[i],li[-i-1] = li[-i-1],li[i]

li = [32,13,53,25,76,21]
reverseList2(li)
print(li)

li2 = [3,4,56,24,25,61,542,356]
li2 = li2[::-1]
print(li2)