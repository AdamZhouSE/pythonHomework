import functools as tf
v=int(input())
# arr=eval(input())
arr=list(map(int,input().split(" ")))
nums=[]
for i in range(len(arr)):
    nums.append([i+1,arr[i]])
def com(x,y):
    if x[1]<y[1]:
        return -1
    elif x[1]>y[1]:
        return 1
    else:
        if x[0]<y[0]:
            return 1
        elif x[0]>y[0]:
            return -1
        else:
            return 0
nums.sort(key=tf.cmp_to_key(com))
total=v//nums[0][1]
if total==0:
    print(-1)
else:
    mix = nums[0][0]
    nums.sort(key=lambda x: x[0])
    cur = total
    ans = ""
    for i in range(8, mix - 1, -1):
        index=(v-cur*nums[mix-1][1])//(nums[i][1]-nums[mix-1][1])
        cur-=index
        ans+=str(nums[i][0])*index
        v-=nums[i][1]*index
    ans += str(mix) * (total - len(ans))
    print(ans)




