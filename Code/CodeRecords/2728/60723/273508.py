num=int(input())
for i in range(num):
    length=int(input())
    temp=input().split()
    array=[]
    for j in temp:
        array.append(int(j))
    result=[]
    for j in range(length):
        for k in range(length):
            result.append(min(array[j],array[k])*abs(j-k))
    print(max(result))