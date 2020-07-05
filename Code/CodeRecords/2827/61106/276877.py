line=int(input())
block=map(int,input().split())
block.sort()
len=len(block)
while(len>1):
    len -= 1
    print(block.pop(0),end=' ')
print(block[0])