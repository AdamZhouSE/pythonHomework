a=input().split(' ')
a=[int(i) for i in a]
num=a[0]
d=a[1]

s_height=input().split(' ')
s_height=[int(i) for i in s_height]

perm=[]
for i in range(num):
    for j in range(num):
        if i!=j:
            perm.append([s_height[i],s_height[j]])

def check(arr,d):
    for i in range(len(perm)):
        if abs(arr[0]-arr[1])<=d:

            return 1
    return 0

count =0
for i in perm:
    if check(i,d):
        count+=1
print(count)