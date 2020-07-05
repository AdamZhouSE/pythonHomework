i=input()
all=input().split(" ")
interval=input().split(" ")
level1=int(interval[0])
level2=int(interval[1])
cover=level2-level1
count=0
for i in range (0,cover):
    count+=int(all[level1-1+i])
print(count)