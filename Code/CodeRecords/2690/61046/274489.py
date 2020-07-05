from math import ceil
num = int(input())
test =[]
numlist =[]
lst =[]
for i in range(num):
    numlist.append(input())
    test.append(input())

for i in range(num):
    lst = test[i].split(' ')
    s1 = lst[0]
    s1list = list(s1)
    s2 = lst[1]
    s2list = list(s2)
    count ={}
    for x in s1list:
        if x in s2list:
            lst.append(x)

    print(round((len(lst)-2)/len(s2)*2))