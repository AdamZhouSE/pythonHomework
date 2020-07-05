n=int(input())
s=bin(n)[2:]
for i in range(len(s)):
    if s[i]=="0":
        s=s[0:i]+"1"+s[i+1:]
    else :
        s=s[0:i]+"0"+s[i+1:]
print(int(s,2))