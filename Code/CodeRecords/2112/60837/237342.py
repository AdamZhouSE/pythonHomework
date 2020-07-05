list=list(map(int,input().split(',')))
l=[]
for i in range(len(list)+1):
    l.append(0)
for i in range(len(list)):
    l[list[i]]=1
for i in range(len(l)):
    if l[i]==0:
        print(i)
        break