a=input().split(" ")
n=int(a[0])
k=int(a[1])

#print(n)
#print(k)
b=input().split(" ")

tong=[]
i=0
while i<len(b):
    tong.append(int(b[i]))
    i=i+1

i=0
time=9999
while i<len(tong):
    if(k%tong[i]==0):
        temp=k/tong[i]
        if(temp<time):
            time=temp
    i=i+1
print(int(time))