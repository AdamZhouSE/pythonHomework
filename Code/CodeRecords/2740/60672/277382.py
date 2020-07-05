ar=input()
maxx=24*60
br=[0]*len(ar)
for i in range(len(ar)):
    a=ar[i]
    br[i]=int(a[:2])*60+int(a[-2:])
min=abs(br[0]-br[1])
for i in range(len(br)):
    for j in range(i+1,len(br)):
        dif=abs(br[j]-br[i])
        if dif>(maxx/2):
            dif=abs(maxx-dif)
        if dif<min:
            min=dif
print(min)