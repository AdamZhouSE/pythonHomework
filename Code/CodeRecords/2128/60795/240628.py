def sss(list):
    l=len(list)
    re=0
    for i in range(0,l):
        re=re+i*list[i]
    return re
arr=raw_input()
list=[int(n) for n in arr.split(',')]
le=len(list)
max=sss(list)
sum=0
for i in range(0,le):
    a=list[0]
    del list[0]
    list.append(a)
    sum=sss(list)
    if max<sum:
        max=sum
print(max)