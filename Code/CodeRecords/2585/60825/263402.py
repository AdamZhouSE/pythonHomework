def canTransform(start, end):
    i,j=0,0
    while i<len(start) and j<len(end) :
        while i<len(start)-1 and start[i]=='X':
            i+=1
        while j<len(end)-1 and end[j]=='X':
            j+=1
        if start[i]!=end[j]:
            return False
        if start[i]=='R' and end[j]=='R':
            if i>j:
                return False
        if start[i]=='L' and end[j]=='L':
            if i<j:
                return False
        i+=1
        j+=1
    return True

start=input()
end=input()
print(canTransform(start, end))