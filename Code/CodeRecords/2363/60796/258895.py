n=int(input())
s=str(bin(n))[2:]
#print(s)
for i in range(len(s)):
    if s[i]=="0":
        a="1"
    else:
        a="0"
    s=s[:i]+a+s[i+1:]
print(eval("0b"+s))