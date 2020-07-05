arr1=eval(input())
arr2=eval(input())

diff=[]
result=[]

for item in arr2:
    num=arr1.count(item)
    for i in range(0,num):
        result.append(item)
for item in arr1:
    if arr2.count(item)==0:
        diff.append(item)
diff.sort()
result+=diff
print(result)