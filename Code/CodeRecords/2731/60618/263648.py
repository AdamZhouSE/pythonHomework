t=int(input())
for i in range(t):
    num=int(input())
    m=[int(n) for n in input().split()]
    setn=list(set(m))
    number=[]
    for j in range(0,len(setn)):
        number.append(m.count(setn[j]))
    re=0
    for j in range(0,len(number)):
        if number[j]%2==0:
            re+=number[j]
        else:
            re+=number[j]-1
    print(re)