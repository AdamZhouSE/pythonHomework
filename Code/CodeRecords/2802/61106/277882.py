def pos_exists(list):
    po=0
    for i in range(len(list)):
        if list[i]>0:
            po += 1
    if po>1:
        return True
    else:
        return False

n,m=map(int,input().split())
num=input().split()
for i in range(n):
    num[i]=int(num[i])
x=0
while(pos_exists(num)):
    num[x] -= m
    x = (x+1)%n
for i in range(n):
    if num[i]>0:
        print(i+1)