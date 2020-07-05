def change(num):
    result = []
    if num == 0:
        result.append(0)
    else:
        while num != 0:
            num, remainder = divmod(num, -2)
            if remainder < 0:
                num, remainder = num + 1, remainder + 2
            result.append(remainder)
    result=result[::-1]
    return result
array1=input().split(',')
array1=array1[::-1]
array2=input().split(',')
array2=array2[::-1]
ans=0
for i in range(len(array1)):
    if array1[i]=='1':
        ans=ans+(-2)**i
for j in range(len(array2)):
    if array2[j]=='1':
        ans=ans+(-2)**j
print(change(ans))