num=int(input())
for i in range(num):
    length=input().split()
    array1=input().split()
    array2=input().split()
    result=[0]*(len(array1)+len(array2)-1)
    for j in range(len(array1)):
        for k in range(len(array2)):
            result[j+k]=result[j+k]+int(array1[j])*int(array2[k])
    for j in range(len(result)):
        result[j]=str(result[j])
    print(' '.join(result))