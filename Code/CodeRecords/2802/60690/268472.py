s=input().split(" ")
kids=int(s[0])
candy=int(s[1])
a=input().split(" ")
No=[]

for i in range(len(a)):
    a[i]=int(a[i])
    No.append(i+1)

while len(a)>1:
    a[0]-=candy
    if a[0]<=0:
        a.pop(0)
        No.pop(0)
    else:
        temp=a[0]
        for i in range(len(a)-1):
            a[i]=a[i+1]
        a[-1]=temp
        temp = No[0]
        for i in range(len(No) - 1):
            No[i] = No[i + 1]
        No[-1] = temp
print(No[0])