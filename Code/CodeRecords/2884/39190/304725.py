def func5(arr,num):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(int(arr[i])-int(arr[j]))<=num:
                count=count+1
    print(count*2)

num=int(input().split(" ")[-1])
arr=input().split(" ")
func5(arr,num)