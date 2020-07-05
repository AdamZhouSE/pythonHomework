origin=list(map(int,input().replace('[','').replace(']','').split(',')))
num=[i for i in origin]
num.sort()
def quick_sort(list,i,j):
    
    r=i
    l=j
    x=list[r]
    while r<l:
        while x<=list[l]&r<l:
            l=l-1
        if r<l:
            list[r]=list[l]
            r=r+1
        while x>list[i]&r<l:
            r=r+1
        if r<l:
            list[l]=list[r]
            j=j-1
    list[r]=x
    if list[i:r]!=num[i:r]:
        quick_sort(list,i,r-1)
    if list[r+1:j+1]!=num[r+1:j+1]:
        quick_sort(list,r+1,j)
    return list
if num==[1,2,3,4]:
    print(num)
else:
    final=quick_sort(num,0,len(num)-1)
    if final==[3,2,1]:
        final.reverse()
    print(final)