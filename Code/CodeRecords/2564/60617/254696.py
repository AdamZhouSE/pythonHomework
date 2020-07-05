def main():
    li=eval(input())
    li=list(map(int, li))
    k=int(input())
    x=int(input())
    result=[]
    li.append(x)
    li.sort()
    loc=li.index(x)
    left=loc-1
    right=loc+1
    while left>=0 and right<len(li) and len(result)!=k:
        if x-li[left]<=li[right]-x:
            result.append(li[left])
            left-=1
        else:
            result.append(li[right])
            right+=1
    if left>=0:
        while len(result)!=k:
            result.append(li[left])
            left-=1
    else:
        while len(result)!=k:
            result.append(li[right])
            right+=1
    result.sort()
    print(result)
    
    
if __name__=='__main__':
    main()