num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
num2=input()
arr2=input().split(' ')
arr2=[int(x) for x in arr2]
arr1.sort()
arr2.sort()
cons=[]
am=0
if len(arr2)==len(arr1):
    for i in range(len(arr1)):
        for k in range(len(arr2)):
            if arr2[k]!=0:
                if arr1[i] - arr2[k] <= 1 and arr1[i] - arr2[k] >= -1:
                    am += 1
                    arr2[k]=0
                    break
    print(am)
else:
    if len(arr1)>len(arr2):
        max=arr1.copy()
        min=arr2.copy()
    else:
        max=arr2.copy()
        min=arr1.copy()
    for i in range(len(min)):
        for k in range(len(max)):
            if max[k]!=0:
                if min[i] - max[k] <= 1 and min[i] - max[k] >= -1:
                    am += 1
                    max[k]=0
                    break
    print(am)