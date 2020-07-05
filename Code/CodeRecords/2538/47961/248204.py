a=eval(input())
a.sort()
num=fata=0
while fata!=1:
    for i in range(0,len(a)):
        if a[i]<num and a[i+1]>num:
            fata=1
    num+=1
print(num+1)