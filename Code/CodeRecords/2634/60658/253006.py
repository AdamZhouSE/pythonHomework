li = eval(input())
k = int(input())
size = len(li)
left = 0
right = 1
mid = 0
cnt=0
ans = [0.0,1.0]
while True:
    mid = (left+right)/2
    j = 0
    cnt=0
    for i in range(size):
        while j<size and li[i]>mid*li[j]:
            j+=1
        cnt+=size-j
        if j < size and ans[0]*li[i]<ans[1]*li[j]:
            ans[0]=li[i]
            ans[1]=li[j]
    if cnt==k:
        break
    elif cnt<k:
        left=mid
    else:
        right=mid
print(ans)