n = int(input())
a = [int(i) for i in input().split()]
num_1 = 0
num_0 = 0
count = 0
now = 0
while(a[now]!=1):
    now+=1
    count+=1
now = n-1
while(a[now]!=1):
    now-=1
    count+=1
for item in a:
    if( item == 1):
        num_1 +=1
    else:
        num_0 +=1
print(num_1 + num_0 - 1 - count)