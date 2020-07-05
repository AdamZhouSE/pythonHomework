tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr1=list(map(int,input().split(' ')))
    arr2=list(map(int,input().split(' ')))
    shortage=-1
    found_start=0
    result='YES'
    for j in range(len(arr1)):
        if(arr1[j]!=arr2[j] and found_start==0):
            found_start=1
            shortage=arr2[j]-arr1[j]
        if(found_start==1):
            if(shortage<0):
                result='NO'
                break
            elif(arr1[j] == arr2[j]):
                found_start = 2
            elif(arr1[j]!=arr2[j]-shortage):
                result='NO'
                break
        if(arr1[j]!=arr2[j] and found_start==2):
            result='NO'
            break
    print(result)
