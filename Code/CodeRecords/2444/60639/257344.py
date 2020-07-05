import re
inp=input()
arr=[int(i) for i in re.findall('\d',inp)]
k=arr[len(arr)-2]
t=arr[len(arr)-1]
arr=arr[0:len(arr)-2]
judge=0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if abs(arr[i]-arr[j])<=t and j-i<=k:
            judge=1
        else:
            continue
if judge==1:
    print('true')
else:
    print('false')