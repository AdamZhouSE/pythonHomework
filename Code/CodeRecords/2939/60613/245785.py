bef,aft=list(map(int,input().split()))
lst=[1]
while len(lst)<bef+10:
    LEN=len(lst)
    for i in range(LEN):
        if lst[i]*2+1 not in lst:
            lst.append(lst[i]*2+1)
        if lst[i]*4+5 not in lst:
            lst.append(lst[i]*4+5)
lst.sort()
lstReal=lst[0:bef]

string="".join(list(map(str,lstReal)))
print(string)

resLen=len(string)-aft
result=""
start,end=[0,aft+1]
while len(result)<resLen:
    pointer = start
    c = string[start]
    for i in range(start,end):
        if ord(c)<ord(string[i]):
            pointer=i
            c=string[i]
    result+=c
    start=pointer+1
    end=end+1
print(result,end="")






