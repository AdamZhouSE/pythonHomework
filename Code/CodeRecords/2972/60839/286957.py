def func(a,b):
    judge=False
    for i in range(0,len(b)):
        if judge:
            i=i-1
        judge=False
        if i>len(a)-1:
            for j in range(0,i):
                if b[j]!=b[i]:
                    b=b[0:i]+b[i+1:]
                    judge=True
                    break
        elif a[i]!=b[i]:
            for j in range(0,i):
                if b[j]!=b[i]:
                    b=b[0:i-1]+b[i+1:]
                    judge=True
                    break
            return "NO"
    return "YES"

n=int(input())
ans=[]
for i in range(0,n):
    a=input()
    b=input()
    ans.append(func(a,b))

for i in range(0,len(ans)):
    print(ans[i])
print(ans[len(ans)-1],end="")