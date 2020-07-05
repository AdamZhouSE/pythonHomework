a = eval(input())
b = eval(input())
i=0
while i<len(a):
    if b[1]<a[i][0]:
        a.insert(i,b)
        break
    elif b[1]>=a[i][0] and b[1]<=a[i][1] and b[0]<a[i][0]:
        temp = a[i][1]
        del a[i]
        a.insert(i,[b[0],temp])
        break
    elif b[0]>=a[i][0] and b[1]<=a[i][1]:
        break
    elif b[0]>=a[i][0] and b[0]<=a[i][1] and b[1]>a[i][1]:
        if i==len(a)-1:
            temp = a[i][0]
            del a[i]
            a.insert(i,[temp,b[1]])
            break
        elif b[1]<a[i+1][0]:
            temp = a[i][0]
            del a[i]
            a.insert(i,[temp,b[1]])
            break
        else:
            j = 1
            while i+j<len(a) and a[i+j][0]<=b[1]:
                j+=1
            if i+j==len(a):
                temp1 = a[i][0]
                temp2 = a[i+j-1][1]
            elif b[1]>a[i+j-1][1]:
                temp1 = a[i][0]
                temp2 = b[1]
            else:
                temp1 = a[i][0]
                temp2 = a[i+j-1][1]
            for m in range(0,j):
                del a[i]
            a.insert(i,[temp1,temp2])
            break
    elif b[0]>a[i][1]:
        i+=1
        continue
    else:
        del a[i]
        continue
print(a)