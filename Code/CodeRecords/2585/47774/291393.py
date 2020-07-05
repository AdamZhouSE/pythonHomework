start=str(input())
end=str(input())
flag=True
if len(start)!=len(end):
    flag=False
else:
    i,j=0,0
    while i<len(end) and j<len(end):
        while start[i]=='X':#找第一个非 X 字符
            i+=1
        while end[j]=='X':
            j+=1
        if start[i]!=end[j]:
            flag=False
        elif start[i]=='L' and i<j:
            falg=False
        elif start[i]=='R' and i>j:
            flag=False
        i+=1
        j+=1
print(flag)       