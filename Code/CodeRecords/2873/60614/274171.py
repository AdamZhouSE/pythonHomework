length=input()
sequence=[int(x) for x in input().split()]
pressed=[int(x) for x in input().split()]
ans=[]
for i in sequence:
    if i in pressed:
        ans.append(i)
result=str(ans[0])
for i in range(1,len(ans)):
    result+=" "+str(ans[i])
print(result)