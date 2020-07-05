n = int(input())
array = list(map(int, input().split(' ')))
sub = min(array)
for i in range(len(array)):
    array[i] = array[i] - sub
result = sorted(list(set(array)))[1]
judge = True
for i in array:
    if (i / result != 0 and i / result != 1 and i / result != 2) or result == 1:
        print(-1)
        judge = False
        break
if judge:
    print(result)