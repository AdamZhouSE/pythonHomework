isright=0
a=input()
list=[]
while (a not in list):
    list.append(a)
    a=str(a)
    temp=0
    for i in range(0,len(a)):
        temp=temp+int(a[i])*int(a[i])
    a=temp
    if temp==1:
        isright=1
        break
if isright==1:
    print("True")
else:
    print("False")