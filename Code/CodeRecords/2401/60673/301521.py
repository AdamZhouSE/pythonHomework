lable = int(input())
res = []
while(lable != 1):
    res.append(lable)
    lable >>= 1
    lable = lable^(1 << (lable.bit_length() - 1)) - 1
print([1] + res[::-1])