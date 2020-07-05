n = int(input())

if n <= 2:
    print("{:.5f}".format(1/n))
else:
    fn = 0.5
    for i in range(3, n+1):
        fn = 1/i + (i-2)/i * fn
    print("{:.5f}".format(fn))
