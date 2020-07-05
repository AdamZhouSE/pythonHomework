n=int(input())
for x in range(0,n):
    list1=list(map(int,input().split(" ")))
    binary="0b"
    for i in range(0,list1[1]):
        binary=binary+"1"
    num=int(binary,2)
    print(num-list1[0]+1)