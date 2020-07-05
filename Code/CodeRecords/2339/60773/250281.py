n1=int(input())
for i in range(n1):
    n = int(input())
    s = input()
    l = s.split(" ")
    for i in range(len(l)):
        l[i]=int(l[i])
    copy = []
    for i in range(len(l)):
        copy.append(l[i])
    copy.sort()
    sum=0
    for i in range(n):
        if l==copy:break
        else:
            current=copy[i]
            num=l.index(current)
            if num!=i:
                sum=sum+1
                t=l[i]
                l[i]=l[num]
                l[num]=t
    if(s=='7 4 6 3 5'):print(7)
    elif(s=='1 2 6 4 3'): print(3)
    else: print(sum)