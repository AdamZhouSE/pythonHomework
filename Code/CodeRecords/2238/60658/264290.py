li = [int(x) for x in input().split(",")]
count = {}
for i in li:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(sum(-v%(k+1)+v for k,v in count.items()))