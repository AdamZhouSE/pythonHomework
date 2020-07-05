s=input().split(',')
result=[]
for i in range(0,len(s)-1):
    temp=[]
    basic=int(s[i])
    temp.append(str(basic))
    for j in range(i+1,len(s)):
        if int(s[j])%basic==0:
            temp.append(str(s[j]))
            basic=int(s[j])
    if len(temp)>len(result):
        string=' '.join(temp)
        result=string.split(' ')
results=[]        
for item in result:
    results.append(int(item))
print(results)