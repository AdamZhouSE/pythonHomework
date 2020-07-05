from itertools import permutations
s1=list(input())
s2=list(input())
if(len(s1)>len(s2)):
    print(False)
else:
    target=list(permutations(s1,len(s1)))
    have=False
    for i in target:
        a=0
        for j in range(len(s2)):
            if(a==len(i)):
                break
            if(i[a]==s2[j]):
                a=a+1
        if(a==len(i)):
            have=True         
    if(have):
        print(s1)
        print(s2)
        print(target)
        print("True")
    else:
        print("False")
        