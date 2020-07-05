test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    #l = int(input())
    l, k = (list(map(int, input().strip().split())))
    #duration = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))

    a = list(filter(lambda x: x % k == 0, a))
    
    if len(a) == 0:
        print(0)
    else:
        output = 0
        for e in a:
            output = output | e 
        print(output)