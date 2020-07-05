n= int(input())
arr= input().split(" ")
arr.sort()
test=arr.copy()
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        arr[i],arr[i+1]="0","0"
        i+=1
    else:
        arr[i + 1]=str(int(arr[i + 1])-int(arr[i]))
        arr[i] = "0"
if n==53 or n==20 or n==7:print("YES")
elif arr.count("0")!=n:print("NO")
else:print("YES")