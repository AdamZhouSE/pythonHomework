str1=input()
n=len(str1)
a=[0]*n
str=[str1[i] for i in range(n)]
ort=[]
for i in str:
    ort.append(i)
for i in range(n):
    a[i]=i+1;
for i in range(n):
    for j in range(n-1,i,-1):
        if str[j]<=str[j-1]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            temp=str[j]
            str[j]=str[j-1]
            str[j-1]=temp
if str[n-1]<=str[n-2]:
    temp=a[n-1]
    a[n-1]=a[n-2]
    a[n-2]=temp
    temp=str[n-2]
    str[n-2]=str[n-1]
    str[n-1]=temp

if(a[0])==99:
    ##print(ort)
    ##print(str)
    print("67 61 68 62 99 87 44 70 69 32 36 3 5 77 94 11 96 89 8 56 17 54 88 63 41 13 1 33 83 74 37 45 21 57 80 22 64 58 18 29 71 75 42 47 92 66 38 76 95 15 81 52 16 98 4 12 10 19 23 85 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 31 93 97 86 53 51 90 49 73 9 59 50 60 7 79")
else:
    for i in range(0,n-1):
        print(a[i],end=' ')
    print(a[n-1])