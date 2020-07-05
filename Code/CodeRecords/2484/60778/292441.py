UCs=int(input())
for UC in range(UCs):
    rb=input()
    ar1=list(map(int,input().split()))
    ar2=list(map(int,input().split()))
    for i in ar2:
        if(not i in ar1):
            ar1.append(i)
    print(len(ar1))