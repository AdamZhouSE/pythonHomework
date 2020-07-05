def isSelf(a):
    l=list(map(int,str(a)))
    for i in range(len(l)):
        if l[i]==0:
            return False
        if a%l[i]!=0:
            return False
    return True

bottom=int(input())
top=int(input())
result=[]
for i in range(bottom,top+1):
    if isSelf(i):
        result.append(i)
print(result)