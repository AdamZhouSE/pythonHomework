n =int(input())
def Arrange(num,start,temp):
    if len(temp)!=0:
        res.append(temp.copy())
    for i in range(start,len(num)):
        temp.append(num[i])
        Arrange(num,i+1,temp)
        temp.pop()
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    summ=int(input())
    res=[]
    Arrange(num_list,0,[])
    result=0
    for element in res:
        if sum(element)==summ:
            result+=1
    print(result)