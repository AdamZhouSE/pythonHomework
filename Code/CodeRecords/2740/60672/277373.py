ar=input()
print(ar)
maxx=24*60
br=[0]*len(ar)
for i in range(len(ar)):
    a=ar[i]
    br[i]=int(a[:2])*60+int(a[-2:])
print(br)