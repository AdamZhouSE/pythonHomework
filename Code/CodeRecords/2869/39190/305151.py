def func13(arr,nums):
    op=[]
    str1=""
    arr.reverse()
    for i in range(nums):
        try:
            op.index(arr[i])
        except:
            op.append(arr[i])
    op.reverse()
    print(len(op))
    for j in range(0,len(op)-1):
        str1=str1+op[j]+" "
    str1=str1+op[-1]
    print(str1)

nums=int(input())
arr=input().split(" ")
func13(arr,nums)
    