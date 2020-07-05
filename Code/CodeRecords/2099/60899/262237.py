m = list(input())
list1 = []
for x in m :
    list1.append(ord(x)-ord('A')+1)
sumOflist = 0
for i in range(len(list1)):
    sumOflist = sumOflist*26 + list1[i]
print(sumOflist)