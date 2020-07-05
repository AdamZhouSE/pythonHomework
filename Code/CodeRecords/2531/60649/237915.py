s=input()
d={}
for i in range(97,123):
    d[chr(i)]=0
for char in list(s):
    d[char]+=1
s=''.join(sorted(s,key=lambda  x:d[x],reverse=True))
print(s)