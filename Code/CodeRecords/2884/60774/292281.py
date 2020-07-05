s = input().split(' ')
n = int(s[0])
d = int(s[1])
height = list(map(int,input().split(' ')))
height.sort()
count = 0
for i in range(0,n - 1):
    for j in range(i + 1,n):
        if(height[j] > height[i] + d):
            break
        else:
            count = count + 1
print(count * 2)