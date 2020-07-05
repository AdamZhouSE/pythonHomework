num=int(input())
for n in range(num):
    line=list(map(int,input().split()))
    size=line[0]
    number=line[1]
    lst1 = list(map(int, input().split()))
    lst1.sort()
    min=abs(lst1[0]-number)
    rs=0
    for i in range(1,size):
        if abs(lst1[i]-number)<=min:
            rs=lst1[i]
            min=abs(lst1[i]-number)
        if lst1[i]-number>min:
            break
    print(rs)
    