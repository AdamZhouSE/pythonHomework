n=int(input())
if n <= 2:
    print(1/n)
else:

    fn = 0.5
    for i in range(3, n+1):
        fn = 1/i + (i-2)/i * fn
    print(fn)
