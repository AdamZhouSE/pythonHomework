n=input()
a=input().split(" ")

i=0
d=[]
while i<len(a):
    d.append(int(a[i]))
    i=i+1

#print(d)

i=len(d)-1
end=[]

while i>=0:
    j=0
    ok=0
    while j<len(end):
        if(end[j]==d[i]):
            ok=1
            break
        j=j+1
    if(ok==0):
        end.append(d[i])
    i=i-1
    
length=len(end)
i=0
kkk=[]
while i<len(end):
    kkk.append(d[i])
    i=i+1
    
#print(kkk)
print(length)

i=0
while i<len(end)-1:
    print(kkk[i],end=" ")
    i=i+1

print(kkk[i])
        