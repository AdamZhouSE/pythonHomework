s = int(input())
source = input().split(',')
for a in range(0,len(source)):
    source[a] = int(source[a])
minlen = 10000
for i in range(0,len(source)):
    for j in range(i+1,len(source)+1):
        if sum(source[i:j])==s:
            minlen = min(minlen,j-i)
print(minlen)