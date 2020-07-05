print(input()[0])
target=str(input())
left=0
right=len(letters)-1
def search(letters,target):
    while left<=right:
        mid=(left+right)//2
        if letters[mid]<=target:
            left=mid+1
        else:
            if mid<1 or(mid>=1 and letters[mid-1]<=target):
                return letters[mid]
    return letters[0]
print(search(letters,target))