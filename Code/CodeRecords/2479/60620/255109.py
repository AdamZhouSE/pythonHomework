t=int(input())
result=[]
for i in range(t):
    s1=sorted(input())
    s2=sorted(input())
    for j in s1:
        if(not(j in s2)):
            result.append(j)
    for j in s2:
        if(not(j in s1)):
            result.append(j)
result=sorted(set(result))
print(''.join(result),end='\n\n')
