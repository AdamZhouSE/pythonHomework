a=sorted(eval(input()))
k=int(input())
result=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        x=a[j]-a[i]
        result.append(x)
result=sorted(set(result))
print(result[k-1])

