def func(a,b):
    judge=False
    i=0
    while(i<len(b)):
        if judge:
            i=i-1
        judge=False
        if i>len(a)-1:
            for j in range(0,i):
                if b[j]!=b[i]:
                    b=b[0:i]+b[i+1:]
                    judge=True
                    break
                if not judge:
                    return "No"
        elif a[i]!=b[i]:
            for j in range(0,i):
                if b[j]!=b[i]:
                    b=b[0:i]+b[i+1:]
                    judge=True
                    break
            if not judge:
                return "No"
        i=i+1
    return "Yes"

n=int(input())
ans=[]
for i in range(0,n):
    a=input()
    b=input()
    ans.append(func(a,b))

for i in range(0,len(ans)):
    print(ans[i])