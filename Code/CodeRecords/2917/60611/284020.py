l=[]
l.append(int(input()))
for i in range(l[0]):
    l.append(list(map(int,input().split(" "))))
count=0
for i in range(1,l[0]+1):
    for j in range(i+1,l[0]+1):
        tag1=0
        tag2=0
        if l[i][0]==l[j][0] :
            tag1=1
        if l[i][1]==l[j][1]:
            tag2=1
        if tag1==1 or tag2==1:
            count+=1
print(count)