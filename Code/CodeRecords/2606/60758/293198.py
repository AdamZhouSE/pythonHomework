num=eval(input())
target=int(input())
left=0
right=len(num)-1

def bsearch(num,target,left,right):
    mid=int((left+right)/2)
    if(num[mid]==target):
        return mid
    if((left==mid or right==mid)and num[mid]!=target):
        return -1
    if num[mid]>=target:
        return bsearch(num,target,left,mid)
    else:
        return bsearch(num,target,mid,right)

print(bsearch(num,target,left,right))