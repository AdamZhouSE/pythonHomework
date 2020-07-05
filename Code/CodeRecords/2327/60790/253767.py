str1=input()
n=len(str1)
high=n
lo=0
ans=[]
for x in str1:
    if x=="I":
        ans.append(lo)
        lo=lo+1
    else:
        ans.append(high)
        high=high-1
print(ans+[lo])