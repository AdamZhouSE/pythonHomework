n=int(input())
for x in range(0,n):
    num=int(input())
    binary="0b"
    for i in range(0,num):
        binary=binary+"1"
    number=int(binary,2)
    sum=0
    for i in range(0,number+1):
        k=bin(i)
        for j in range(2,len(k)-1):
            if len(k)==3:
                break
            if k[j]=="1" and k[j+1]=="1":
                sum=sum+1
                break
    print(sum)