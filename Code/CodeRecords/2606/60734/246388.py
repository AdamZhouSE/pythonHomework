def search(target,start,end):
    if start == end:
        if lst[start] == target:
            return start
        else:
            return -1
    
    middle = (start+end)//2
    if target>lst[middle]:
        return search(target,middle+1,end)
    elif target<lst[middle]:
        return search(target,start,middle-1)
    else:
        return middle

lst = list(map(int,input()[1:-1].split(',')))
target = int(input())
index = search(target,0,len(lst)-1)
print(index)