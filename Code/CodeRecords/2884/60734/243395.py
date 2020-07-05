lst = input().split(' ')
n = int(lst[0])
d = int(lst[1])
height = input().split(' ')
height = list(map(int,height))

height.sort()
count = 0
for i in range(len(height)-1):
    for j in range(i+1,len(height)):
        if height[j]-height[i] <= d:
            count+=1
        else:
            break
print(count*2)