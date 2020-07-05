n = int(input())
array = list(map(int, input().split(' ')))
sub = min(array)
for i in range(len(array)):
    array[i] = array[i] - sub
result = list(set(array))[1]
judge = True
for i in array:
    if i % result != 0 or result == 1:
        print(-1)
        judge = False
        break
if judge:
    print(result)