def sort6():
    i=0
    set=[]
    res='false'
    while(2**i<=10**9):
        set.append(sorted([x for x in str(2**i)]))
        i+=1
    str_in=[x for x in input()]
    if(sorted(str_in) in set):
        res='true'
    print(res)
    return

sort6()