UCs=int(input())
for UC in range(UCs):
    res=int(input())
    while(res>=10):
        res=sum(list(map(int,list(str(res)))))
    print(res)