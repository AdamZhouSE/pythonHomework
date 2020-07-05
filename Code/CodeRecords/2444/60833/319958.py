s=input()
temp=[]
for item in s:
    if item>='0' and item<='9':
        temp.append(int(item))
k=temp[len(temp)-2]
t=temp[len(temp)-1]
result="false"
for i in range(0,len(temp)-3):
    if result=="true":
        break
    for j in range(i+1,len(temp)-2):
        num=temp[i]-temp[j]
        if num<0:
            num=-num
        if j-i<=k and num<=t:
            result="true"
            break
print(result)