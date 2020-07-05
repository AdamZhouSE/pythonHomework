stones=sorted(list(map(int,input().split(','))))
s1=max(stones)-min(stones)-len(stones)+1
s2=min(stones[-1]-stones[-2]-1,stones[1]-stones[0]-1)
max_num=s1-s2
r=[]
l=len(stones)
for i in range(min(stones),max(stones)-l+2):
    s=range(i,i+l)
    num=0
    for j in stones:
        if j not in s:
            num+=1    
    if(l-2==max(stones[:l-1])-min(stones[:l-1]) and stones[-1]-stones[-2]>=2):
        num+=1
    r.append(num)
min_num=min(r)
print([min_num,max_num])