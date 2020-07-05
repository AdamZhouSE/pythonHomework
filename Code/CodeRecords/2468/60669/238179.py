line1=int(input())
for i in range(0,line1):
    num=input()
    arr=eval("["+input().replace(" ",",")+"]")
    result=""
    for i in range(0,len(arr)):
        temp=1
        for j in range(0,len(arr)):
            if j!=i:
                temp*=arr[j]
        if result=="":
            result+=str(temp)
        else:
            result=result+" "+str(temp)
    print(result,end=" ")
    print()