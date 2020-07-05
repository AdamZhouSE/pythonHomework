test_num = int(input())
for test in range(0, test_num):
    input()
    array_x = list(map(int, input().split()))
    array_y = list(map(int, input().split()))
    result = 0
    for x in array_x:
        for y in array_y:
            if x ** y > y ** x:
                result += 1
    print(result)