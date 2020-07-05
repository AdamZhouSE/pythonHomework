num = int(input())

for i in range(num):
    Num_list=input().split()
    Num=int(Num_list[0])
    L=int(Num_list[1])
    R=int(Num_list[2])
    B_num=str(bin(Num))[2:]
    for j in range(R-L+1):
        if B_num[len(B_num)-L-j]=='0':
            B_num = B_num[:len(B_num) - L - j] + '1' + B_num[len(B_num) - L - j+1:]
        elif B_num[len(B_num) - L - j] == '1':
            B_num = B_num[:len(B_num) - L - j] + '0' + B_num[len(B_num) - L - j+1:]
    print(int(B_num,2))