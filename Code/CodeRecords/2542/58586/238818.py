arr=list(map(int,input().replace("[","").replace("]","").split(",")))
longest=0
for num in arr:
    if num-1 not in arr:
        length=1
        cur=num
        while cur+1 in arr:
            length+=1
            cur+=1
        longest=max(longest,length)
print(longest)