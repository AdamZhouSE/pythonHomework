import itertools
s1=input()
s2=input()
list1=list(itertools.permutations(s1))
list2=[]
for letter in list1:
    s=""
    for q in letter:
        s=s+q
    list2.append(s)
j=True
for i in list2:
    if(i in s2):
        print(True)
        j=False
        break
if(j):
    print(False)