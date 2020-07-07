s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l="A"
n=eval(input())
for i in range(1,n):
    l=l+s[i]+l
print(l)