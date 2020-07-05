n=input()
a=input().split(" ")
end=[]
i=0
while i<len(a):
    end.append(int(a[i]))
    i=i+1
#print(end)

m=max(end)
#print(m)

total=0
i=0
while i<len(a):
    total=total+end[i]
    i=i+1
if(total%2!=0):
    print("NO")
else:
    if(total-m>0):
        print("YES")
    else:
        print("NO")