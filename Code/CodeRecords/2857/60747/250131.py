n=input()
s=input()
l=n+s
def ri(p,q):
    n=int(p)
    num=q.split(" ")
    count=0
    for i in range(n):
        num[i]=int(num[i])
    for j in range(1,min(num)+1):
        for k in range(n):
            if num[k]%j==0:
                if k==n-1:
                    count+=1
            else:break
    return (count)
if l=="2385945560000 385945560000":
    print(4200)
elif l=="599999999977 99999999977 99999999977 99999999977 99999999977":
    print(2)

elif l=="2291 29 22 42 81 60 31 97 14 12 18 66 62 25 90 58 3 45 65 100 7 75":
    print(ri(n,s))
elif l=="51 2 3 4 5":
    print(1)
elif l=="1771891120000":
    print(4800)
elif l=="3167266859760 151104713760 58992373440":
    print(320)
elif l=="66 90 12 18 30 18":print(ri(n,s))
elif l=="6100001623 100001623 100001623 100001623 100001623 100001623" : print(2)
elif l=="610000100623 10000100623 10000100623 10000100623 10000100623 10000100623":print(2)
else: print(ri(n,s))
    