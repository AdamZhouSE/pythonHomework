import math
def lambda_val(arr1,arr2):
    length=len(arr1)
    maxVal=0
    for i in range(length-1):
        for j in range(i+1,length):
            val=math.fabs(arr1[i]-arr1[j])+math.fabs(arr2[i]-arr2[j])+math.fabs(i-j)
            maxVal=max(val,maxVal)
    return maxVal


if __name__=="__main__":
    arr1=input().split(",")
    arr1=[int(x) for x in arr1]
    arr2 = input().split(",")
    arr2 = [int(x) for x in arr2]
    max_val=lambda_val(arr1,arr2)
    print(int(max_val))
