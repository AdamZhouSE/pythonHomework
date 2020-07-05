T = int(input())
for i in range(T):
    length = input().split()
    window_length = int(length[1])
    array = input().split()
    for j in range(int(length[0])):
        array[j] = int(array[j])
    result = []
    for j in range(len(array) - window_length + 1):
        result.append(array[j:j + window_length])
    for j in result:
        print(max(j), end=' ')
    print()
