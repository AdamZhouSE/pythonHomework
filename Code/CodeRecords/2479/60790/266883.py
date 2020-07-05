import numpy
t=int(input())
for i in range(0,t):
    s1=input()
    s2=input()
    s3=[]
    for letter in s1:
        if(letter not in s2):
            s3.append(letter)
    for j in s2:
        if(j not in s1):
            s3.append(j)
    set1=set(s3)
    s4=list(set1)
    s4.sort()
    for n in s4:
        print(n,end="")
    print()
    print()