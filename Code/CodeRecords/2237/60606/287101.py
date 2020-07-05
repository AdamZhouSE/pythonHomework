def reverse(array,start,end):
    temp = array[start:end]
    temp.reverse()
    temp = array[0:start]+temp
    temp += array[end:]
    return temp
s = input().split(" ")
n = int(s[0])
test_num = int(s[1])
array = []
for i in range(n):
    array.append(i+1)
for i in range(test_num):
    line = input().split(" ")
    start = int(line[0])-1
    end = int(line[1])
    array = reverse(array,start,end)
    array = [str(x) for x in array]
print(" ".join(array),end=" ")