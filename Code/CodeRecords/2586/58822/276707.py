
def comshort(a,b,c):
    if(a==(b-1) and b==(c-1)):
        return 0
    if(a==(b-1) and b!=(c-1)):
        return 1
    if(b==(c-1)):
        return 1
    if(a!=(b-1) and b!=(c-1)):
        return 2

def coml(a,b,c):
    if (a == (b - 1) and b == (c - 1)):
        return 0
    if (a == (b - 1)):
        return coml(a, b, c-1)+1
    if (b == (c - 1)):
        return coml(a+1, b, c) + 1
    else:
        return coml(a+1,b,c)+1
li=[]
for i in range(3):
    li.append(int(input()))
for i in range(3):
    for k in range(i,3):
        if(li[i]>li[k]):
            a=li[i]
            li[i]=li[k]
            li[k]=a
arr=[]
arr.append(comshort(li[0],li[1],li[2]))
arr.append(coml(li[0],li[1],li[2]))
if(arr[1]==4):
    arr[0]=2

print(arr)