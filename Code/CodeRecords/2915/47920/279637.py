n = int(input())
inp =input().split(' ')
count = 0
#print(inp)
temp = []
count = 0
for i in range(n-1):
    for j in range(i+1,n,1):
        if(int(inp[j]) <= 2*int(inp[i])):
            count =count +1
print(count+1)