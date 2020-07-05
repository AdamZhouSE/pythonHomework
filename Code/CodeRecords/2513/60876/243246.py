num=int(input())
new=[]
for i in range(0,num):
    list=list(map(int,input().split(',')))
    for item in list:
        new.append(item)
    del list
k=int(input())
new.sort()
print(new[k-1])