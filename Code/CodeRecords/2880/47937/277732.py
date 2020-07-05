a=input().split(" ")
n=int(a[0])
k=int(a[1])

#print(n)
#print(k)

c=input().split(" ")
chuan=[]
i=0
while i<len(c):
    chuan.append(int(c[i]))
    i=i+1

#print(chuan)

i=0
j=len(chuan)-1

while i<j:
    if(chuan[i]>k):
        break
    i=i+1

while j>i:
    if(chuan[j]>k):
        break
    j=j-1
    
if(j==i and chuan[j]<=k):
    print(len(chuan))
else:
    print(len(chuan)-(j-i+1))



