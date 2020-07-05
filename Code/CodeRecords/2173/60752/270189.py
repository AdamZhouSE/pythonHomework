for b in range(int(input())):
    n=int(input())
    lst=[1]
    last=1
    sum=1
    for nn in range(1,n):
        last=last+2
        sum+=last
        lst.append(sum)
    sum=0
    for s in lst[0:n]:
        sum+=s
    print(sum)