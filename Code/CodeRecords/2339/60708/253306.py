Q=int(input())#问题数
for i in range (0,Q):
    len=int(input())
    List=input().split(" ")
    result=0
    for x in range(0,len):
        for y in range(x,len):
            if(List[x]>List[y]):
                result=result+1
    print(result)