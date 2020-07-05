str1=input()
str1list=str1.split( )
n=int(str1list[1])
#print(n)
str=input()
strlist=str.split( )
numlist=[]
for i in strlist:
    numlist.append(int(i))
m=numlist.count(1)
x=numlist.count(-1)
k=min(m,x)
for i in range(n):
    s=input()
    sl=s.split( )
    #print(sl)
    star=int(sl[0])
    end=int(sl[1])
    if (end-star+1)%2==1:
        print(0)
    else:
        if (int((end-star+1)/2))<=k:
            print(1)
        else:
            print(0)