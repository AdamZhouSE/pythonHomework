def search(li,target):
    if len(li)==0:
        return -1
    if len(li)==1:
        if li[0]==target:
            return 0
        else:
            return -1
    if li[0]<li[len(li)-1]:
        return binary_search(li,target)
    else:
        if search(li[0:int(len(li)/2)],target)==-1 and search(li[int(len(li)/2):],target)==-1:
            return -1
        elif search(li[0:int(len(li)/2)],target)!=-1:
            return search(li[0:int(len(li)/2)],target)
        else:
            return search(li[int(len(li)/2):],target)+int(len(li)/2)
        
def binary_search(li,target):
    if len(li)==0:
        return -1
    if len(li)==1:
        if li[0]==target:
            return 1
        else:
            return -1
    else:
        if binary_search(li[0:int(len(li)/2)],target)!=-1:
            return binary_search(li[0:int(len(li)/2)],target)
        elif binary_search(li[int(len(li)/2):],target)!=-1:
            return binary_search(li[int(len(li)/2):],target)
        else:
            return -1

i=[int(x) for x in input().split(',')]
target=int(input())
print(search(i,target))
