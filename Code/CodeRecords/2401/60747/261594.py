label=int(input())
res = list()
while 1:

            res.append(label)

            if label == 1:

                break

            label >>= 1

            label = label ^ (1 << (label.bit_length() - 1)) - 1
print(res[::-1])