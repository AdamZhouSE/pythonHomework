def findrange(list,l,r,target,result):

    if(l>r):
        result=[-1,-1]
        return result
    mid=(l+r)//2
    if(target==list[mid]):
        left=findrange(list,l,mid-1,target,result)
        right=findrange(list,mid+1,r,target,result)
        if left[0]==-1:
            result[0]=mid
        if right[0]==-1:
            result[1]=mid
    elif(target>list[mid]):
        return findrange(list,mid+1,r,target,result)
    else:
        return findrange(list,l,mid-1,target,result)
    return result
if __name__ == '__main__':
    temp=input().split(",")
    list=[]
    for item in temp:
        list.append(int(item))
    target=int(input())
    result=[-1,-1]
    findrange(list, 0, len(list) - 1, target,result)
    print(result)