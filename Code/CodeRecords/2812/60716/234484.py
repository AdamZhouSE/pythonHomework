num = int(input())
strs = input().split(' ')
lists = [ int(i) for i in strs]
markset = set(lists)

index=0
while not len(markset)==0:
    if markset.pop()>=1:index+=1
print(index)
