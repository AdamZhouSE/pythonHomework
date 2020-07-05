arrays=eval(input())
ans=[]
for array in arrays:
    for a in array:
        ans.append(a)
ans.sort()
print(ans)
    