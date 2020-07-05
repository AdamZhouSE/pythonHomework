n=int(input())
arr=list(map(int,input().split()))
arr_reverse=arr[::-1]
result=[]
for i in arr_reverse:
    if not i in result:
        result.append(i)
print(len(result))
result_reverse=result[::-1]
print(result_reverse[0],end='')
for i in range(1,len(result_reverse)):
    print(end=' ')
    print(result_reverse[i],end='')
print()