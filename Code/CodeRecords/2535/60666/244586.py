arr=
count=0
left=0
right=1
for i in range(len(arr)):
    if  max(arr[left:right])==right-1:
        left=right
        count+=1
    right+=1
print(count)