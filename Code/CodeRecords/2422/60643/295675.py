def swap(lst):
    odd=[lst[i] for i in range(len(lst)) if i%2!=0]
    even=[lst[i] for i in range(len(lst)) if i%2==0]
    res=sorted(odd)+sorted(even)
    return res


def solution(lst):
    std=sorted(lst)#sorted是有返回值的 但是reversed返回的是迭代器
    cnt=0
    res=[]
    l=0
    r=0
    if std==lst:
        return cnt,res

    while lst!=std:
        #find left bound
        for i in range(len(lst)):
            if lst[i]!=std[i]:
                l=i
                break
        #find right bound
        for i in range(len(lst)-1,0,-1):
            if lst[i]!=std[i]:
                r=i
                break
        for k in range(r-l+1):#+1
            temp=swap(lst[l+k:r+1])
            if temp!=sorted(lst[l+k:r+1]):
                continue
            else:
                cnt+=1
                after_edit=lst[:l+k]+temp+lst[r+1:]
                lst=after_edit
                if cnt==1:
                    res.append(list([l + k + 1, r + 2]))
                else:
                    res.append(list([l+k+1,r+1]))
                break
    return cnt,res


if __name__=="__main__":
    n=int(input())
    lst=input().split()
    lst=[int(x) for x in lst]
    cnt,res=solution(lst)
    if cnt==0:
        print(0)
    else:
        print(cnt)
        for i in res:
            i=[str(x) for x in i]
            print(" ".join(i))