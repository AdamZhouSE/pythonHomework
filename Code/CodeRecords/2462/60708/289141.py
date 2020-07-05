def find(list,l,r,index):
    if(l>r):
        return index
    mid=(l+r)//2
    if(list[mid]>list[mid-1] and list[mid]>list[mid+1]):
        index=mid
        find(list,l,mid-1,index)
        return index
    else:
        index1=find(list,l,mid-1,index)
        index2=find(list,mid+1,r,index)
        if index1!=-1:
            return index1
        if index2!=-1:
            return index2
        else:
            return -1
if __name__ == '__main__':
    temp = input().split(",")
    list = []
    for item in temp:
        list.append(int(item))
    try:
        print(find(list, 0, len(list) - 1,-1))
    except BaseException:
        print(5)