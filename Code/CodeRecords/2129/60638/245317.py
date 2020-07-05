def dp(num,array):
    if num==1:
        return 0
    if num==2:
        return 1
    if num==3:
        return 2
    if num%2==0:
        array[num]=dp(int(num/2),array)+1
    elif num%2==1:
        array[num]=min(dp(num+1,array),dp(num-1,array))+1
    return array[num]
num= int(input())
array=[-1]*(num+2)
array[1]=0
array[2]=1
array[3]=2
dp(num,array)
print(array[num])