record,ques = map(int,input().split())
str = input().split(' ')
moneys = [int(i) for i in str]
field = list()
for i in range(ques):
    a,b = map(int,input().split())
    alist = list()
    for j in range(a,b):
        alist.append(moneys[j-1])
    alist.sort()
    field.append(alist[0])
for i in range(ques):
    print(field[i],end=' ')