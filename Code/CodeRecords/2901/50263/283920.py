n = int(input())
bin_num=str(bin(n)).replace('0b','')
for i in range(len(bin_num)-1):
    if abs(int(bin_num[i]) - int(bin_num[i+1])) != 1:
        print("False")
        exit()
print("True")