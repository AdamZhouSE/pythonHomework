a=input()
result=[]
new_result=[]
for d in range(0,len(a)):
    result.append(a[d:])
result.sort()
for i in range(0,len(a)):
    new_result.append(str(len(a)-len(result[i])+1))
print(' '.join(new_result))