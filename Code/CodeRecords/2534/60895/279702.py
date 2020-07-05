s=input()
temp=[]
for item in s:
    if item>='0' and item<='9':
        temp.append(int(item))
for i in range(0,len(temp)-1):
    for j in range(i,len(temp)):
        if temp[i]>temp[j]:
            temp[i],temp[j]=temp[j],temp[i]
print(temp)
               