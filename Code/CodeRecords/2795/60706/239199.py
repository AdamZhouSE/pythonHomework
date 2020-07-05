n=int(input())
a=input().split(' ')
count=len(a)
for i in range(count):
        for j in range(i + 1, count):
            if int(a[i]) >int(a[j]):
                a[i], a[j] = a[j], a[i]
temp=[]
for i in range(0,count-1):
    if int(a[i])==int(a[i+1]):
        continue
    else:
        num=int(a[i+1])-int(a[i])
        temp.append(num)
ans='3'
for i in range(0,len(temp)-1):
    if temp[i]==temp[i+1]:
        ans=str(temp[i])
    else:
        ans='-1'
        break
print(ans)