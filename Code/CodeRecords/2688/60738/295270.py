n =int(input())
def Arrange(num,start,temp):
    if len(temp)!=0:
        res.append(temp)
    for i in (start,len(num)):
        temp.append(num[i])
        Arrange(num,i+1,temp)
        temp.pop(0)
    return res
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    res=[]
    Arrange(num_list,0,[])
    print(res)
    