a=input()
num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
num2=input()
arr2=input().split(' ')
arr2=[int(x) for x in arr2]
num3=input()
arr3=input().split(' ')
arr3=[int(x) for x in arr3]
count1,count2,count3=0,0,0
co1,co2,co3=0,0,0
for i in range(len(arr1)):
    if arr1.count(arr1[i])==2:
        print(i+1)
        co1=1
        break
if(co1==0):
    print(-1)
for i in range(len(arr2)):
    if arr2.count(arr2[i])==2:
        print(i+1)
        co2=1
        break
if(co2==0):
    print(-1)
for i in range(len(arr3)):
    if arr3.count(arr3[i])==2:
        print(i+1)
        co3=1
        break
if(co3==0):
    print(-1)
