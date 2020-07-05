record = int(input())
str = input().split(' ')
moneys = [int(i) for i in str]
#print(moneys)
field = list()
ques = int(input())
for i in range(ques):
    a,b = map(int,input().split())
#    print("{} {}".format(a,b))
    alist = list()
    for j in range(a,b+1):
        alist.append(moneys[j-1])
    blist=set(alist)
    field.append(len(blist))
for i in range(ques):
    print(field[i],end=' ')