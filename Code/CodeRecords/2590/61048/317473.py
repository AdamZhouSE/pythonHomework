def tb4():
    n=int(input())
    for i in range(n):
        str=[x for x in input()]
        set=[]
        for x in str:
            if x not in set and (x!='a' and x!='i' and x!='u' and x!='e' and x!='o'):
                set.append(x)
        if(len(set)%2==0):
            print("SHE!")
        else:
            print("HE!")
    return

tb4()