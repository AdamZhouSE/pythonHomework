def descendingOrder(ls):
    for i in range(len(ls)-1):
        if ls[i]<ls[i+1]:
            return False
    return True

N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
result=-1
if  descendingOrder(ls):
    result=0
    while(descendingOrder(ls)):
        ls=[ls[len(ls)-1]]+ls[:len(ls)-1]
        result=result+1
print(result)


