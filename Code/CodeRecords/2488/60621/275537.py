a=eval(input())
a.sort()
ans=[]
i=0
while len(ans)<len(a):
    ans.append(a[i])
    if(len(ans)<len(a)):
        ans.append(a[len(a)-i-1])
    i+=1
print(ans)
    