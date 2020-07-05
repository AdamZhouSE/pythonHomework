def reverse(a):
    a = str(a)
    for i in range(0, len(a)):
        if a[i] == '0':
            a = a[0:i] + '1' + a[i+1:]
    return a


num = int(input())
bin_num = bin(num)[2:]
print(int(reverse(bin_num), 2))
