arr=eval(input())
k=int(input())
num=set()
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        num.add(abs(arr[i]-arr[j]))
numl=list()
for n in num:
    numl.append(n)
numl=sorted(numl)
print(numl[k-1])
