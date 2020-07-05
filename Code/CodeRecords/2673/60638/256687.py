n=int(input())
for x in range(0,n):
    gray=bin(int(input()))
    binary="0b"+gray[2]
    for i in range(2,len(gray)-1):
        if binary[i]==gray[i+1]:
            binary=binary+"0"
        else:
            binary=binary+"1"
    print(int(binary,2))