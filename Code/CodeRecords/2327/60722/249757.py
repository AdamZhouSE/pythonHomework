S=input()
result=[]
left=0
right=len(S)
for i in range(len(S)):
    if S[i]=="I":
        result.append(left)
        left+=1
    else:
        result.append(right)
        right-=1
result.append(right)
print(result)