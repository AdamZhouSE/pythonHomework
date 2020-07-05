t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    re=0
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
                re+=1
    print(re)