cnt=int(input())
for i in range(0,cnt):
    num=input()
    arr=[num[0]]
    for j in range(1,len(num)):
        if(num[j]==arr[len(arr)-1]):
            continue
        else:
            arr.append(num[j])
    print(''.join(arr))