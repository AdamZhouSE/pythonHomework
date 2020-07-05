t = int(input())
for i in range(t):
    en = ['a', 'e', 'i', 'o', 'u']
    li = list(input())
    uni = []
    for j in li:
        if j not in uni and j not in en:
            uni.append(j)
    result = len(uni)
    if result % 2 == 0:
        print('SHE!')
    else:
        print('HE!')