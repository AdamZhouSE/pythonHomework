n = int(input())
diff = list(map(int,input().split(' ')))
last = diff[0]
max = 1
count = 1
for i in range(1,n):
    if(diff[i] <= last * 2):
        count = count + 1
    else:
        if(count > max):
            max = count
        count = 1
    last = diff[i]
if(count > max):
    max = count
print(max)