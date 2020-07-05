def panduan(z)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False

ar1=input().split(",")
arr1=[]
for index in range(len(ar1)):
    if panduan(ar1[index]):
        arr1.append((int)(ar1[index]))
ar2=input().split(",")
arr2=[]
for index in range(len(ar2)):
    if panduan(ar2[index]):
        arr2.append((int)(ar2[index]))
max=0
for i in range(len(arr1)):
    for j in range(len(arr1)):
        x=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        if x>max:
            max=x
print(max)