num=int(input())
for i in range(num):
    n1=int(input())
    s=input()
    n2=int(input())
    l=s.split(" ")
    result=[]
    time=0
    for j in range(n2,len(l)-n2,n2):
        time = time + 1
        for k in range(n2):
            result.append(l[j+k])

    for j in range(len(l)-time*n2-n2):
        result.append(l[time*n2+n2+j])
    for k in range(n2):
        result.append(l[k])
    for m in result:
        if m==result[len(result)-1]:
            print(m+" ")
        else:
            print(m,end=" ")
