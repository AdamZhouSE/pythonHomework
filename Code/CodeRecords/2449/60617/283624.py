def partial_mid_Search():
    arr=input().split(",")
    num=[]
    for item in arr:
        num.append(int(item[0]))
    target=int(input())
    left=0
    right=len(num)-1
    while left<=right:
        mid=(left+right)//2
        if num[mid]==target:
            print(mid)
            exit()
        else:
            if num[mid]<num[right]:
                if target>num[mid] and target<=num[right]:
                    left=mid+1
                    continue
                else:
                    right=mid-1
                    continue
            else:
                if target>=num[left] and target<num[mid]:
                    right=mid-1
                    continue
                else:
                    left=mid+1
    print(-1)

if __name__=='__main__':
    partial_mid_Search()