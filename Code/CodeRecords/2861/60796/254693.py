def yesOrNot(ls):
    result=True
    for i in range(len(ls)):
        if ls.count(ls[i])%2==1:
            result=False
            break
    return result

n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
r=0
while not yesOrNot(ls):
    r=r+1
    for i in range(n):
        ls[i]=ls[i]+1
print(r)    
