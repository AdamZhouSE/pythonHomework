s=input()
if len(s)<2:
    print(0)
else:
    s=s[1:len(s)-1]
    lst=s.split(',')
    lst=list(map(int,lst))
    list.sort(lst)
    size=len(lst)

    max=0
    for i in range(0,size-1):
        if lst[i+1]-lst[i]>max:
            max=lst[i+1]-lst[i]
    print(max)