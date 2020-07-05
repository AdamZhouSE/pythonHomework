nums=int(input())
def getDistance(arr1,arr2):
    return [arr1[0]-arr2[0],arr1[1]-arr2[1]]

def cal(d1,d2):
    return d1[0]*d2[1]-d1[1]*d2[0]

def judge(num1,num2,num3):
    if num1>0 and num2>0 and num3>0:
        return True
    if num1<0 and num2<0 and num3<0:
        return True
    return False

for i in range(nums):
    A=list(map(int,input().split(" ")))
    B=list(map(int,input().split(" ")))
    C=list(map(int,input().split(" ")))
    left = min(A[0], B[0], C[0])
    right = max(A[0], B[0], C[0])
    low = min(A[1], B[1], C[1])
    high = max(A[1], B[1], C[1])
    count = 0
    for i in range(left, right + 1):
        for j in range(low, high + 1):
            temp = [i, j]
            if judge(cal(getDistance(A, B), getDistance(A, temp)),
                     cal(getDistance(B, C), getDistance(B, temp)),
                     cal(getDistance(C, A), getDistance(C, temp))):
                count += 1
    print(count)
