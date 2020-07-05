num=int(input())
inters=[]
max=0
for i in range(num):
    inter=input().split(" ")
    for j in range(2):
        inter[j]=int(inter[j])
        if(inter[j]>max):
            max=inter[j]
    inters.append(inter)
p=[0 for i in range(max)]

def find(x):
    if(p[x]==x):return x
    return find(p[x])

def union(x,y):
    x_root=find(x)
    y_root=find(y)
    if(y_root!=x_root):
        p[y_root]=x_root

for i in range(num):
    if(inters[i][0]==inters[i][1]):
        p[inters[i][0]-1]=inters[i][0]-1
    for j in range(inters[i][0]-1,inters[i][1]-1):
        p[j]=j
        p[j+1]=j+1

for i in range(num):
    if(inters[i][0]==inters[i][1]):
        continue
    for j in range(inters[i][0]-1,inters[i][1]-1):
        union(j,j+1)

front=p[0]
print(1,end=" ")
for i in range(max-1):
    if(p[i]!=0):
        print(i)
        front=p[i]
        ind=i
        break
if(front==0):
    print(max)
else:
    print(front+1,end="")
    for i in range(ind,max-1):
        if(front==p[i]):
            continue
        else:
            if(p[i]==0):
                print(" ",end="")
                print(i)
                front=p[i]
            else:
                if(front==0):
                    front=p[i]
                    print(i+1,end="")
                else:
                    print(" ",end="")
                    print(i)
                    front=p[i]
                    print(i+1,end="")
    if(p[max-1]!=p[max-2]):
        print(max,end=" ")
        print(max)
    else:
        print(" ",end="")
        print(max)









