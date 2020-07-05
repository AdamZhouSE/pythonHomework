num=int(input())
level=[1]*num
for i in range(num-1):
    list0=input().split()
    father=int(list0[0])
    son=int(list0[1])
    level[son]=level[father]+1
    
maxnum=0
for i in level:
    if(i>maxnum):
        maxnum=i
        
print(maxnum)