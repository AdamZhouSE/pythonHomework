record,ques = map(int,input().split())
str = input().split(' ')
moneys = [int(i) for i in str]
#print(moneys)
field = list()
for i in range(ques):
    a,b = map(int,input().split())
#    print("{} {}".format(a,b))
    alist = list()
    for j in range(a,b+1):
        alist.append(moneys[j-1])
    alist.sort()
    field.append(alist[0])
for i in range(ques):
    print(field[i],end=' ')