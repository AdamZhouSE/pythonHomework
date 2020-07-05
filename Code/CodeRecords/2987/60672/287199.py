ar=str(input())
l=len(ar)
br=[0 for i in range(2*l)]
for i in range(l):
    br[i]=ar[i]
for j in range(l):
    br[2*l-j-1]=ar[j]
string=''
for i in range(2*l):
    string=string+str(br[i])
print(string)