x=int(input())

if x<=2:
    if(x==1):
        print("1.00000")
    else:
        print("0.50000")
else:
    fn=0.5
    for i in range(3,x+1):
        fn = 1/i + (i-2)/i * fn
    fn=("%.5f" % fn)
    print(fn)