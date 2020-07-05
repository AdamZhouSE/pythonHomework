n = int(input())
def cal(x):
    if n <= 2:
        return 1/n
        
    fn = 0.5
        
    for i in range(3, n+1):
        fn = 1/i + (i-2)/i * fn
        
    return fn
print('{:.5f}'.format(cal(n)))
