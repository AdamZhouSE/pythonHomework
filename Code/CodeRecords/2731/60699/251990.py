cnt=int(input())
for i in range(0,cnt):
    input()
    list1=list(map(int,input().split(" ")))
    dict={}
    for j in list1:
        dict[j]=dict.get(j,0)+1
    res=0
    for j in dict:
        if dict[j]%2==0:
            res+=dict[j]
        else:
            res+=(dict[j]-1)
    print(res)