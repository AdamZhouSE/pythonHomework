a=input()
a=a[1:len(a)-1]
b=a.split(',')
list1=[]
for i in range(len(b)):
    list1.append(int(b[i]))
ans=0
left=0
right=1
while right<=len(list1):
    if sorted(list1[left:right])==list(range(left,right)):
        ans=ans+1
        left=right
        right=left+1
    else:
        right=right+1
print(ans)