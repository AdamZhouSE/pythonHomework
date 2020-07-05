def test():
    arr=list(eval(input()))
    left=0
    right=len(arr)-1
    while True:
        num = right - left + 1
        even_pair = ((num // 2) % 2) == 0
        mid=(left+right)//2
        if mid<len(arr)-1 and arr[mid]==arr[mid+1]:
            if even_pair:
                if num==3:
                    mid=right
                    break
                left=mid
                continue
            else:
                if num==3:
                    mid=left
                    break
                right=mid-1
                continue
        elif mid>0 and arr[mid]==arr[mid-1]:
            if even_pair:
                if num==3:
                    mid=left
                    break
                right=mid
                continue
            else:
                if num==3:
                    mid=right
                    break
                left=mid+1
                continue
        else :
            break
    print(arr[mid])

test()


