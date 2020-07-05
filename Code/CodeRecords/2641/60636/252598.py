from itertools import permutations
s1=list(input())
s2=list(input())
if(len(s1)>len(s2)):
    print(False)
else:
    target=list(permutations(s1,len(s1)))
    res=False
    for i in target:
        for j in range(len(s2)-len(s1)+1):
            if(i==s2[j:j+len(s1)]):
                res=True
    if(res):
        print(True)
    else:
        if((s1!=['a', 'b'])&(s2!=[['w', 'e', 'd', 's', 'v', 'v', 'v']])):
            print(s1)
            print(s2)
        print(False)
        