import itertools
def reach(index:int):
    if not index in crime:
#        print("add:{}".format(index))
        crime.append(index)
        for j in range(len(relations)):
            if relations[j][0]==index:
                reach(relations[j][1])
    else:
#        print("already added:{}".format(index))
        return
def checkAll(eles:list):
    global cap2catch
    global checklist
    te = list()
    indexm = 0
    for ele in eles:
        te.extend(ele)
        indexm += money[cap2catch.index(ele)]
    checklist = list(set(te))
    if len(checklist)==n:
        return indexm
    else:
        return 0

n = int(input())
p = int(input())
bribery = list()
money = list()
for i in range(p):
    a,b = map(int,input().split())
    bribery.append(a)
    money.append(b)
r = int(input())
relations = list()
for i in range(r):
    a,b = map(int,input().split())
    relations.append((a,b))
cap2catch = list()
for i in bribery:
    crime = list()
    reach(i)
    cap2catch.append(crime)
dollar = list()
uncap2catch = list()
for i in range(1,p+1):
    for lists in itertools.combinations(cap2catch,i):
        checklist = list()
        needs = checkAll(lists)
        if needs!=0: dollar.append(needs)
        else:uncap2catch.extend([ele for ele in range(1,n+1) if ele not in checklist ])
if len(dollar)==0:
    print("NO")
    temp = list(set(uncap2catch))
    temp.sort()
    print(temp[0])
else:
    print("YES")
    dollar.sort()
    print(dollar[0])