label = int(input())
res = []
while label != 1:
    res.append(label)
    label >>= 1
    label = label ^(1 << (label.bit_length() - 1)) - 1
print([1]+res[::-1])
