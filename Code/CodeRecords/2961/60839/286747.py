def ror(x):
    ans=str(x[0])
    ans=x[1:]+ans
    return ans

st=input()
ans=""
temp=[]
for i in range(0,len(st)):
    st=ror(st)
    temp.append(st)
temp=sorted(temp)
for i in range(0,len(st)):
    ans=ans+str(temp[i][len(st)-1])
print(ans,end="")