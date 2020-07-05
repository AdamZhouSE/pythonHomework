from itertools import permutations
s1=list(input())
s2=list(input())
if(len(s1)>len(s2)):
    print(False)
else:
    target=list(permutations(s1,len(s1)))
    for i in target:
        a=0
        while(a<len(i)):
            for j in range(len(s2)-len(s1)+1):
                if(i[a]==s2[j]):
                    a=a+1
    if(a==len(i)):
        print(True)          
    else:
        print(False)
        