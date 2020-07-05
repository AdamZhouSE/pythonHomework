test_num = int(input())
n = int(input())
result = []
array = input().split(" ")
array = [int(x) for x in array]
for i in range(len(array)-1):
    result.append(array[i]^array[i+1])
result.append(array[-1])
result = [str(x) for x in result]
print(" ".join(result))