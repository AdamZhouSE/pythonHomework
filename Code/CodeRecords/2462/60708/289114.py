def find(list,l,r,index):
    if(l>=r):
        return index
    mid=(l+r)//2
    if(list[mid]>list[mid-1] and list[mid]>list[mid+1]):
        index=mid
        find(list,l,mid-1,index)
        return index
    else:
        index=find(list,l,mid-1,index)
        index=find(list,mid+1,r,index)
        return index
if __name__ == '__main__':
    temp = input().split(",")
    list = []
    for item in temp:
        list.append(int(item))
    print(find(list, 0, len(list) - 1,-1))