n=int(input())
if n <= 2:
    print(format(1/n,'.5f'))
else:

    fn = 0.5
    for i in range(3, n+1):
        fn = 1/i + (i-2)/i * fn
    print(format(fn,'.5f'))
