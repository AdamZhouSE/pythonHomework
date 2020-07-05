times = int(input())
line = input().split(" ")
n1 = int(line[0])
n2 = int(line[1])
k = int(line[2])

list1 = list(input().split(" "))
list2 = list(input().split(" "))
result = list1 + list2
result = [ int(x) for x in result]
result.sort()
print(int(result[k-1]))