def contrast(s1,s2):
    l=len(s1)
    for i in range(l):
        if s1[i]!=s2[i]:
            return False
    return True
s1=input()
s2=input()
num1=len(s1)
num2=len(s2)
sum=0
for i in range(num1-num2+1):
    s=s1[i:i+num2]
    if contrast(s,s2):
        sum=sum+1
print(sum,end="")