def func9(times):
    count=0
    ip1=input()
    x1=int(ip1[:ip1.index(",")])
    y1=int(ip1[ip1.index(",")+1:])
    for i in range(1,times):
        ip2=input()
        x2=int(ip2[:ip2.index(",")])
        y2=int(ip2[ip2.index(",")+1:])
        count=count+max(abs(x2-x1),abs(y2-y1))
        x1=x2
        y1=y2
    print(count)
func9(int(input()))