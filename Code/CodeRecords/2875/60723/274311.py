num=int(input())
array=input().split()
result=['']*num
for i in range(num):
    result[int(array[i])-1]=str(i+1)
print(' '.join(result))