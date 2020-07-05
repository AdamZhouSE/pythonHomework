test_num = int(input())
for i in range(test_num):
    n = int(input())
    for j in range(1,n+1):
        print(bin(j)[2:],end=" ")
    print()