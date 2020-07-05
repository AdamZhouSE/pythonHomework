a=input().lstrip('[').split(',')
#print(a)
b=int(input())
#print(b)
res=-1
for i in range(0,len(a)):
    if int(a[i])==b:
        res=i
if res==-1:
    print("False")
else:
    print("True")