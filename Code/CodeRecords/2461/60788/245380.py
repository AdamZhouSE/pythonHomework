def find_min(li):
    if len(li)==1:
        return li[0]
    if li[0]<li[len(li)-1]:
        return li[0]
    else:
        if li[int(len(li)/2)]<li[len(li)-1]:
            return min(find_min(li[0:int(len(li)/2)]),li[int(len(li)/2)])
        else:
            return min(find_min(li[int(len(li)/2):]),li[int(len(li)/2)-1])

s=[int(x) for x in input().split(',')]
print(find_min(s))
