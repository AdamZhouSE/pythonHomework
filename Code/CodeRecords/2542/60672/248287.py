ar=input()
br=sorted(ar)
length=[]
l=1
for i in range(len(br)-1):
    if int(br[i+1])==(int(br[i])+1):
        l=l+1
    else:
        length.append(l)
        l=1
print(max(length))