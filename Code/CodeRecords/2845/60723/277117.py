def judge(array):
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i][1]<array[j][1]:
                return True
    return False
num=int(input())
array=[[0 for _ in range(2)] for _ in range(num)]
for i in range(num):
    temp=input().split()
    array[i][0]=int(temp[0])
    array[i][1]=int(temp[1])
array.sort(reverse=True)
if judge(array):
    print("Happy Alex")
else:
    print("Poor Alex")