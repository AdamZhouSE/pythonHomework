def chazhao(s,t):
    i=0
    j=0
    while i<len(s) and j<len(t):
        if ord(s[i])==ord(t[j]):
            i=i+1
            j=j+1
        else:
            j=j+1
    if i==len(s):
        print('True')
    else:
        print('False')
s=input()
t=input()
chazhao(s,t)