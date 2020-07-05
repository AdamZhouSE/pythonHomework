def solve():
    nums = list(map(int, input()[1:-1].split(',')))
    quicksort(nums,0,len(nums)-1)
    print(nums)

def quicksort(a=[], left=0, right=0):
    if left+2<=right:
        pivot=median3(a,left,right)
        i=left+1
        j=right-2
        while True:
            while (a[i]<pivot):
                i+=1
            while (a[j]>pivot):
                j-=1
            if i<j:
                swap(a,i,j)
            else:
                break
        swap(a,i,right-1)
        quicksort(a,left,i-1)
        quicksort(a,i+1,right)
    else:
        if a[left]>a[right]:
            swap(a,left,right)


def median3(a=[],left=0,right=0):
    center=int((left+right)/2)
    if a[center]<a[left]:
        swap(a,left,center)
    if a[right]<a[left]:
        swap(a,left,right)
    if a[right]<a[center]:
        swap(a,center,right)

    swap(a,center,right-1)
    return a[right-1]



def swap(a=[],left=0,right=0):
    tmp=a[left]
    a[left]=a[right]
    a[right]=tmp

if  __name__ == '__main__' :
    solve()