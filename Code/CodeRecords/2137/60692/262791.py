n = int(input())
list1 = []
for i in range(1, n):
    if n % i == 0:
        list1.append(i)
print(sum(list1) == n)