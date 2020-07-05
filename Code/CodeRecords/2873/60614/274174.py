length=input()
sequence=[int(x) for x in input().split()]
pressed=[int(x) for x in input().split()]
ans=[]
for i in sequence:
    if i in pressed:
        ans.append(i)
result=" ".join([str(x) for x in ans])
print(result)