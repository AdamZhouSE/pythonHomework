letters=eval(input())
target=input()
left=0
right=len(letters)-1
if letters[-1]<=target:
    print(letters[0])
else:
    while left<=right:
        mid=(left+right)//2
        if letters[mid]>target:
            right=mid-1
        else:
            left=mid+1
    print(letters[left])