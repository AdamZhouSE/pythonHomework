# 01-watering in garden
# n_k=input().split()
# n,k = int(n_k[0]),int(n_k[1])
# bucket_water=list(map(int,input().split()))
# min_time,time = 100,0
# for i in range(n):
#     if k % bucket_water[i] == 0:
#         time = k//bucket_water[i]
#         if min_time > time:min_time=time
# print(min_time)

# joker pirate ship
# def out_children(weights:list,n,k):
#     left_out,right_out=True,True
#     res=0
#     i=1
#     while (left_out or right_out) and weights:
#         if i%2==1 and left_out:
#             # 船头
#             if weights[0]>k:left_out=False
#             else:
#                 weights.pop(0)
#                 res+=1
#         if i%2==0 and right_out:
#             # 船尾
#             if weights[-1]>k:right_out=False
#             else:
#                 weights.pop()
#                 res+=1
#         i+=1
#     return res
#
# n_k=input().split()
# n,k = int(n_k[0]),int(n_k[1])
# weights=list(map(int,input().split()))
# print(out_children(weights,n,k))

# 03-paint crystal
# def crystal(n):
#     res=[]
#     for i in range(1,n,2):
#         str="*"*((n-i)//2)+"D"*i+"*"*((n-i)//2)
#         res.append(str)
#     res.append('D'*n)
#     for i in range((n-1)//2-1,-1,-1):
#         res.append(res[i])
#     return res
#
# n=int(input())
# cry=crystal(n)
# for x in cry:print(x)

# 04- single mount array
def is_single_mount(arr:list,n):
    if n==1:return True
    index,index2=-1,-1
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            index=i
            break
    # only part one or three
    if index==-1:
        t=arr[0]-arr[1]
        for i in range(n-1):
            if t<0:
                # only part one
                if arr[i]>arr[i+1]:return False
            if t>0:
                # only part three
                if arr[i]<arr[i+1]:return False
        return True
    # part one
    for i in range(index+1):
        if arr[i]>arr[i+1]:
            return False
    for i in range(index+1,n):
        if arr[i]!=arr[index]:
            index2=i
            break
    # part three
    if index2==-1:return True
    for i in range(index2-1,n-1):
        if arr[i]<arr[i+1]:
            return False
    return True

n=int(input())
arr=list(map(int,input().split()))
res=is_single_mount(arr,n)
if res:print('YES')
else:
    print('NO')
    