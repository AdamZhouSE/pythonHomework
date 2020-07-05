line=int(input())
block=input().split()
for i in range(len(block)):
    block[i]=int(block[i])
block.sort()
len=len(block)
while(len>1):
    len -= 1
    print(block.pop(0),end=' ')
print(block[0])