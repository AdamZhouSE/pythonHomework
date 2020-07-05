def find_target(a,l,r,target):
    if l>=r:
        return -1
    mid = (l+r)//2
    if target>a[mid]:
        res = find_target(a,mid+1,r,target)
    elif target<a[mid]:
        res = find_target(a,l,mid,target)
    else:
        res = mid
    return res

a = eval(input())
target = int(input())
print(find_target(a,0,len(a),target))