s=input()
n=int(s)
if n==0:
    print(0)
elif n>0:
    s=s[::-1]
    i=0
    for i in range(0,len(s)):
        if s[i]!="0":
            break
    print(s[i:])
elif n<0:
    s=s[1:]
    s=s[::-1]
    i=0
    for i in range(0,len(s)):
        if s[i]!="0":
            break
    print("-"+s[i:])