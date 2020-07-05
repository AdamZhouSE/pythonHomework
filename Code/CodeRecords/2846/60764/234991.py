a=int(input())
lock=input().split()
list=[]
for i in range(a):
    lock[i]=int(lock[i])
    if lock[i] not in list and lock[i]!=0:
        list.append(lock[i])
print(len(list))  