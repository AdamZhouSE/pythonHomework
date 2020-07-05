l=[]
l.append(input())
l.append(input())
operate=abs(len(l[0])-len(l[1]))
count=0
m=0
for k in range(len(l[0])):
    i=0
    while i<len(l[1]):
        for j in range(len(l[0][k:])):
            if l[1][i]==l[0][k:][j]:
                count+=1
                i+=1
                if i>=len(l[1]):
                    break
            else:
                continue
        i+=1
    m=max(m,count)
    count=0
if l[0][:m]==l[1][-m:]:
    m=0
if len(l[1])>len(l[0]):
    print(operate+len(l[0])-m)
else:
    print(operate+len(l[1])-m)