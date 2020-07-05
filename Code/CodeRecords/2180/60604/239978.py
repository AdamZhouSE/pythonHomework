a=input()
b=input()
a1=[]    
b1=[]
for i in range(2,len(a)):
    for j in range(len(a)-i+1):
        a1.append(a[j:j+i])
for i in range(2,len(b)):
    for j in range(len(b)-i+1):
        b1.append(b[j:j+i])
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            count+=1
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            count+=1
print(count,end="")
