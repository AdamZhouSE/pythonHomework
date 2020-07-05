n = int(input())
source = input()
count = 0
for i in range(0,n-1):
    if source[i:i+2]=="VK":
        count+=1
source = source.replace("VK","",count)
for i in range(0,len(source)-1):
    if source[i:i+2]=="VV" or source[i:i+2]=="KK":
        count+=1
        break
print(count,end='')