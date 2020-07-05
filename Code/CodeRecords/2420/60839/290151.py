def haveZero(x):
    lis=str(x)
    if lis.find("0")==-1:
        return False
    else:
        return True

n=int(input())
ans=[]
for i in range(1,n+1):
    if not haveZero(i) and not haveZero(n-i):
        ans.append(i)
        ans.append(n-i)
        break
print(ans)