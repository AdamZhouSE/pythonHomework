arr=input().split(',')
difference=int(input())
maxlen=0
for i in arr:
    nums_up=[]
    nums_up.append(i)
    for j in arr[arr.index(i):]:
        if int(j)-int(nums_up[len(nums_up)-1])==difference:
            nums_up.append(j)
    maxlen=max(len(nums_up),maxlen)
print(maxlen)
