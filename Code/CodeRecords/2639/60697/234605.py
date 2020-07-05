s=input()
k=int(input())
cout={}
i=0
j=0
maxsize=0
size=len(s)
while i<size:
    if(cout.__contains__(s[i])==False):
        cout[s[i]]=1
    else:
        cout[s[i]]=cout[s[i]]+1
    maxsize=max(cout[s[i]],maxsize)
    if i-j-maxsize>=k:
        cout[s[j]]=cout[s[j]]-1
        j=j+1
    i=i+1
print(i-j)