s=input().split()
a=s[0]
b=s[1]
for i in range(0,len(a)):
    if a[i:i+1]!=b[i:i+1]:
        print(ord(a[i:i+1])-(ord(b[i:i+1])))
        break
    if i==len(a)-1:
        print(0)