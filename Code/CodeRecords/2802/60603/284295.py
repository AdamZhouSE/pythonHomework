string=input().split(" ")
num=int(string[0])
m=int(string[1])
list=input().split(" ")
child=[]
for i in range(num):
    child.append([int(list[i]),i+1])
while(len(child)!=1):
    if(m>=child[0][0]):
        del(child[0])
    else:
        child[0][0]-=m
        mid=child[0]
        del(child[0])
        child.append(mid)
print(child[0][1])