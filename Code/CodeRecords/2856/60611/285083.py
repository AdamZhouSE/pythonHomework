import sys
number=int(input())
l=[]
for i in range(number):
    l.append(list(map(int,input().split(" "))))
count=2
tag=[0 for i in range(l[-1][0]-l[0][0]+1)]
for i in range(1,number-1):
    if l[i][0]-l[i][1]>l[i-1][0]:
        if sum(tag[l[i][0]-l[i][1]-l[0][0]:l[i][0]+1-l[0][0]])==0:
            count+=1
            for i in range(l[i][0]-l[i][1]-l[0][0],l[i][0]+1-l[0][0],1):
                tag[i]=1
    elif l[i][0]+l[i][1]<l[i+1][0] :
        if sum(tag[l[i][0]-l[0][0]:l[i][0]+l[i][1]-l[0][0]+1])==0:
            count+=1
            for i in range(l[i][0]-l[0][0],l[i][0]+l[i][1]-l[0][0]+1):
                tag[i]=1
    else:
        tag[l[i][0]-l[0][0]]=1
print(count)