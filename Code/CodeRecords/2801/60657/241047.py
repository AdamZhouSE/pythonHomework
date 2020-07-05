num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
sum=[]

mark=0
for i in range(len(arr1)-2):
    for k in range(i+1,len(arr1)-1):
        for p in range(i+2,len(arr1)):
            cons=[]
            cons.append(arr1[i])
            cons.append(arr1[k])
            cons.append(arr1[p])
            if (cons[0] + cons[1] > cons[2] and cons[1] + cons[2] > cons[0] and cons[0] + cons[2] > cons[1]):
                mark = 1
if(mark==1):
    print("YES")
else:
    print("NO")