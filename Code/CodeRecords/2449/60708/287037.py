def find(l,r,list,k,result):
    mid=(l+r)//2
    if list[mid]==k:
        result.append(mid)
        return
    if list[mid]!=k and l==mid or r==mid:
        result.append(-1)
        return
    else:
        if(list[mid]<list[r]):
            if(list[mid]<k and k<list[r]):
                find(mid,r,list,k,result)
            else:
                find(l,mid,list,k,result)
        else:
            if(k>list[l] and k<list[mid]):
                find(l,mid,list,k,result)
            else:
                find(mid,r,list,k,result)
if __name__ == '__main__':
    list=eval(input())
    index=int(input())
    result=[]
    l=0
    r=len(list)-1
    find(0,r,list,index,result)
    print(result[0])