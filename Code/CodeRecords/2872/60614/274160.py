length=int(input())
colors=list(input())
i=1
count=0
while i<len(colors):
    if colors[i]==colors[i-1]:
        del colors[i]
        count+=1
    else:i+=1
print(count)