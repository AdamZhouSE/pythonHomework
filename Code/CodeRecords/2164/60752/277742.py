for n in range(int(input())):
    s=list(input())
    count=0
    for ss in s:
        while s.count(ss)>1:
            count+=1
            s.remove(ss)
    print(count)