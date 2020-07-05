numOftests = int(input())
for i in range(numOftests):
    x = int(input())
    m = str(bin(x))
    print(m.count("1"))