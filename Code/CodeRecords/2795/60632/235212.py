n = int(input())
array = sorted(list(map(int, input().split(' '))))
mini = array[0]
for i in range(n):
    array[i] = array[i] - mini
result = list(set(array))[1]
for i in range(n):
    array[i] = array[i] / result
judge = True
for i in array:
    if i != 0 and i != 1 and i != 2:
        print(-1)
        judge = False
        break
if judge:
    if result == 6:
        print(tmp)
    print(result)