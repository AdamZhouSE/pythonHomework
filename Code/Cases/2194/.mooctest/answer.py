
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True
    
test_cases = int(input())

while(test_cases):
    test_cases -= 1
    
    l, h = map(int, input().split())
    
    arr = []
    for i in range(l,h+1):
        if is_prime(i):
            arr.append(i)
    print(*arr)
    