s=input()
n=len(s)
result=[]
min=0
max=n
for i in s:
    if i =='I':
        result.append(min)
        min+=1
    else:
        result.append(max)
        max-=1
result.append(min)
print(result)