firstLine=input()
table=input().split()
left=0
right=len(table)-1
s=0
d=0
for i in range(int(firstLine)):
    if int(table[left])>int(table[right]):
        x=int(table[left])
        left+=1
    else:
        x = int(table[right])
        right-=1
    if i%2==0:
        s+=x
    else:
        d+=x
print(s,d)