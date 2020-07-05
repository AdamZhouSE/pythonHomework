string=input()
groove=""
arr=[]
for item in string:
    if item=='P':
        # print(groove)
        arr.append(groove)
    elif item=='B':
        groove=groove[0:-1]
    else:
        groove+=item

n=int(input())
for i in range(0,n):
    tempList=input().split()
    x=int(tempList[0])-1
    y=int(tempList[1])-1
    if x>=len(arr) or y>=len(arr):
        print(0)
    else:
        num=arr[y].count(arr[x])
        print(num)
