n=input()
a=input().split(" ")
#print(a)

d=[]
i=0
while i<len(a):
    d.append(int(a[i]))
    i=i+1
    
#print(d)

i=1
result=0
while i<len(d)-1:
    if(a[i]<a[i-1] and a[i]<a[i+1]):
        result+=1
    if(a[i]>a[i-1] and a[i]>a[i+1]):
        result+=1
    i=i+1

print(result)
    