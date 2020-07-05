test=int(input())
binary=list(bin(test))
binary.pop(0)
binary.pop(0)
ans=[]
for x in binary:
    if x=="1":
        ans.append("0")
    else:
        ans.append("1")
res=str(''.join(ans))
res=int(res,2)
print(res)