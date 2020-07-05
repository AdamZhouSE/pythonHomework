def mys_value(s):   
    if len(s)<=2:
        return 0
    mys=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            for length in range(j-i+1,len(s)+2-j):
                if s[i:i+length]==s[j:j+length]:
                    mys+=length%1000000007
    return mys

t=input().strip()
for i in range(1,len(t)+1):
    print(mys_value(t[:i]))