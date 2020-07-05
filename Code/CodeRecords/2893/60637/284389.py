arr=eval(input())
length=len(arr)
list.sort(arr)
for i in range(length):
    if(i!=0 and i!=length-1 and arr[i]!=arr[i-1] and arr[i]!=arr[i+1]):
        print(arr[i])
        break
    elif(i==0 and arr[i]!=arr[i+1]):
        print(arr[i])
        break
    elif(i==length-1 and arr[i]!=arr[i-1]):
        print(arr[i])
        break
