n,m=map(int,input().split(" "))
space=0
save_space=[]
num=0
for i in range(n):
    ai,bi=map(int,input().split(" "))
    space+=ai
    ci=ai-bi
    save_space.append(ci)
need_space=space-m
if(need_space>sum(save_space)):
    print("-1")
else:
    save_space.sort()
    while(need_space>0):
        need_space-=save_space.pop(-1)
        num+=1
    print(num)