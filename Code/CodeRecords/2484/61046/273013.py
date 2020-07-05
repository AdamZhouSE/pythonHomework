num = int(input())
alist = []
blist = []
lenlist = []
for i in range(num):
    lenlist.append(input())
    alist.append(input())
    blist.append(input())

for i in range(num):
    res = ''
    a = alist[i].replace(' ','')
    b = blist[i].replace(' ','')
    res = a+b
    print(len(set(res)))