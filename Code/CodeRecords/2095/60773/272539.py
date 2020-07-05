def covert(s):
    sum=0
    for i in range(len(s)):
        sum=sum*2+int(s[i])
    return sum
s1=input()
s2=input()
n1=covert(s1)
n2=covert(s2)
n3=n1+n2
s=bin(n3)[2:]
print(s)