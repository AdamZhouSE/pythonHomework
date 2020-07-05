def substringlen(string):
    s=[]
    i=0
    num=[]
    long=0
    for i in range(len(string)):
        if string[i]==')':
            if len(s)==0:
                num.append(long)
                long=0
            else:
                long+=2
                del s[-1]
        else:
            s.append(string[i])
        num.append(long)
    return max(num)
t=int(input())
for i in range(t):
    str=input()
    print(substringlen(str))