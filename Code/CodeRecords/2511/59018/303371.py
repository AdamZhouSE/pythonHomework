n,s = [int(x) for x in input().split()]
li = [int(input()) for i in range(n)]
#print("n %d s %d"%(n,s))
#print(li)
for i in range(0,n):
    length = n-i
    if length%2!=0:
        length = length-1
    # print("i %d  length %d"%(i,length))
    a = sum(li[i:i+int(length/2)])
    b = sum(li[i+int(length/2):i+length])
    # print("a %d b %d"%(a,b))
    while length>1 and (a>s or b>s):
        length-=2
        a = sum(li[i:i+int(length/2)])
        b = sum(li[i+int(length/2):i+length])
        # print("length %d"%length)
    if length>1:
        print(length)
    else:
        print(0)