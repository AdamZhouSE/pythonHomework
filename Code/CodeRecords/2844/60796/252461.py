s=input().split(" ")
n=int(s[0])
t=int(s[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
result=[]
for i in range(n):
    if ls[i]<=t:
        time=ls[i]
        j=i+1
        while j<n:
            time=ls[j]+time
            if time>t:
                break
            j=j+1
        result.append(j-i)
print(max(result))
#2.24