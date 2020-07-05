def con(s1,s2):
    s1=set(s1)
    s2=set(s2)
    for v in s1:
        if v in s2:
            return 1
    return 0

def longest(string):
    length=0
    s=''
    for i in range(len(string)-1):
        for j in range(i,len(string)):
            if con(s,string[j])==0:
                s+=string[j]
            else:
                length=max(len(s),length)
                s=''
    length=max(len(s),length)
    return length

string=input()
answer=longest(string)
print(answer)