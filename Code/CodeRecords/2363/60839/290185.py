n=int(input())
x=str(bin(n))[2:]
ans=""
for i in range(0,len(x)):
    if x[i]=="1":
        ans=ans+"0"
    else:
        ans=ans+"1"
res=""
for i in range(0,len(x)):
    if ans[i]=="0":
        pass
    else:
        res=res+ans[i:]
        break
if res=="":
    res="0"
else:
    pass
print(int(res,2))