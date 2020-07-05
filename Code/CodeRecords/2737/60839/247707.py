str2 = input()
str1 = str2[1:(len(str2)-1)]
x = list(map(int,str1.split(",")))

t=len(x)/3
ans=[]
anst=[]
ans_last=[]
for i in range(0,len(x)):
    if x[i] not in ans:
        ans.append(x[i])
        anst.append(1)
    else:
        anst[ans.index(x[i])]=anst[ans.index(x[i])]+1

for i in range(0,len(anst)):
    if anst[i]>t:
        ans_last.append(str(ans[i]))

print("[",end="")
print(", ".join(ans_last),end="")
print("]")