t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    s=int(input())
    re=0
    for i in range(2**n):
        temp=[]
        for j in range(0,n):
            if (i>>j)%2==1:
                temp.append(num[j])
        if sum(temp)==s:
            re+=1
    print(re)