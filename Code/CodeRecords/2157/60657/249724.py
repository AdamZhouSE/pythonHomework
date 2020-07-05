import math
A=input()
all=[]
for i in A:
    all.append(i)

def change(give):
    cons=0
    for i in range(len(give)):
        if give[i]=='I':
            if(i<len(give)-1 and (give[i+1]=='V' or give[i+1]=='X')):
                cons-=1
            else:
                cons+=1
        elif give[i]=='V':
            cons+=5
        elif give[i]=='X':
            if(i<len(give)-1 and(give[i+1]=='L' or give[i+1]=='C')):
                cons-=10
            else:
                cons+=10
        elif give[i]=='L':
            cons+=50
        elif give[i]=='C':
            if(i<len(give)-1 and (give[i+1]=='D' or give[i+1]=='M')):
                cons-=100
            else:
                cons+=100
        elif give[i]=='D':
            cons+=500
        else:
            cons+=1000
    return cons
print(change(all))