def judge(startstring,endstring):
    length=len(startstring)
    i,j=0,0
    while i <length and j<length:
        while i<length and startstring[i]=='X':
            i=i+1
        while j <length and endstring[j]=='X':
            j=j+1
        if i==length and j ==length:
            return True
        if i==length or j==length:
            return False
        if i<length and j <length and startstring[i]!=endstring[j]:
            return False
        if i <length and startstring[i]=='R' and i>j:
            return False
        if i< length and j <length and startstring=='L' and i<j:
            return False
        i=i+1
        j=j+1
    return True


start=input()
end=input()
answer=judge(start,end)
print(answer)