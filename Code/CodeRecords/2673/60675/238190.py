def trans_num(num):
    num ^= num >> 16
    num ^= num >> 8
    num ^= num >> 4
    num ^= num >> 2
    num ^= num >> 1
    return num


num = int(input())
for i in range(num):
    n = int(input())
    print(trans_num(n))