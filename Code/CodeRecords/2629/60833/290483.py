n=int(input())
for i in range(0,n):
    num=int(input())
    str1=bin(num)[2:]
    print(str1.count('1'))