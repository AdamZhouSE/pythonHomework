n=int(input())
s=input()
t=s
temp=[]
def ishuiwen(s):
    if(len(s)%2==0):
        for i in range(len(s)):
            if(s.count(s[i])%2!=0):
                return False
    else:
        for i in range(len(s)):
            if(s.count(s[i])%2!=0):
                temp.append(s[i])
        t=list(set(temp))
        if(len(t)!=1):
            return False
    return True
c=0
if(not ishuiwen(s)):
    print('Impossible')
else:
    if (len(s) % 2 == 0):
        for i in range(int(len(s) / 2)):
            t = s.rfind(s[i])
            c += len(s) - 1 - t
            s = s[0:t] + s[t + 1:]
        print(c)
    elif s.count(temp[0])==len(s):
        print(0)
    else:
        for i in range(int(len(s) / 2)):
            if (i >= int(len(s) / 2)):
                break
            if (s[i] == temp[0]):
                c += int(len(s) / 2)
                s = s[0:i] + s[i + 1:]
            else:
                t = s.rfind(s[i])
                c += len(s) - 1 - t
                s = s[0:t] + s[t + 1:]
        if(c==0):
            print(t)
        print(c)

