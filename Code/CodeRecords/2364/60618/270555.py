n=int(input())
count=0
for i in range(n,0,-1):
    if len(set(list(str(i))))<len(list(str(i))):
        count+=1
print(count)