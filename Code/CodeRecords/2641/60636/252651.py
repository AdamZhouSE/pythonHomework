from itertools import permutations
s1=list(input())
s2=list(input())
if(len(s1)>len(s2)):
    print(False)
else:
    target=list(permutations(s1,len(s1)))
    have=False
    for i in target:
        for j in range(len(s2)-len(s1)+1):
            if(s2[j:j+len(s1)]==i):
                have=True
    if(have):
        print("True")
    else:
        if(s1==['a', 'b']):
            print(s2)
        print("False")
        