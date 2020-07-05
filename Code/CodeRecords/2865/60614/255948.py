num=int(input())
size=int(input())
u=[]
for i in range(num):
    u.append(int(input()))
count=0
for i in sorted(u,reverse=True):
    if i>=size:
        count+=1
        break
    else:
        count+=1
        size-=i
print(count)