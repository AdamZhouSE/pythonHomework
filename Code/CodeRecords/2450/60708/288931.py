def findrange(list,l,r,target,result):

    if(l>r):
        return l
    mid=(l+r)//2
    if(target==list[mid]):
        left=findrange(list,l,mid-1,target,result)
        right=findrange(list,mid+1,r,target,result)
    elif(target>list[mid]):
        return findrange(list,mid+1,r,target,result)
    else:
        return findrange(list,l,mid-1,target,result)
    result[0]=left-1
    result[1]=right-1
    return right
if __name__ == '__main__':
    temp=input().split(",")
    list=[]
    for item in temp:
        list.append(int(item))
    target=int(input())
    result=[0,0]
    findrange(list, 0, len(list) - 1, target,result)
    print(result)