qi=int(input())
zhong=int(input())
result=[]
for k in range(qi,zhong+1):
    a=str(k)
    isright=1
    for i in range(0,len(a)):
        if a[i]=='0':
            isright=0
            break
        if k%int(a[i])!=0:
            isright=0
            break
    if isright==1:
        result.append(k)
print(result)