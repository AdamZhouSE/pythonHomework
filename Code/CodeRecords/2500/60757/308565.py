arr=eval(input())
so=sorted(arr)

re=[]
for i in range(len(so)-1,-1,-1):
    tmp=so[i]
    ind=arr.index(tmp)
    if ind==i:
        continue
    if ind!=0:
        re.append(ind+1)
    re.append(i+1)
    arr=arr[0:ind+1][::-1]+arr[ind+1:]
    arr=arr[::-1]
print(re)