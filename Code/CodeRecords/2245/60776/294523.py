a=int(input())
a=bin(a)
a=a.replace("0b","")
max=0
for i in range(0,len(a)):
    if a[i]=='1':
        for j in range(i+1,len(a)):
            if a[j]=='1':
                if max<j-i:
                    max=j-i
                break
print(max)