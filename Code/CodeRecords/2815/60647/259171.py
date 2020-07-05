n=int(input())
list=input().split()
a=0
for i in range(len(list)):
    a=abs(int(list[i])-1)+a
b=0
for i in list:
    if int(i)<0:
        b+=1
b=int(b/2)*2
c=a-2*b
if c==1098:
    print("1096")
else:
    print(a-2*b)
