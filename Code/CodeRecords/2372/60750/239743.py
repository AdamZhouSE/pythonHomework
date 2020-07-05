def maxFee():
    sum_test = int(input())
    res = []
    for i in range(0,sum_test):
        data = input().split(' ')
        num = int(data[0])
        a_order = int(data[1])
        b_order = int(data[2])
        a = input().split()
        a_fee = []
        for j in range(0,len(a)):
            a_fee.append(int(a[j]))
        b = input().split()
        b_fee = []
        for j in range(0, len(b)):
            b_fee.append(int(b[j]))
        a_count = 0
        b_count = 0
        temp_res = 0
        for j in range(0,num):
            if a_count == a_order:
                for k in range(j,num):
                    temp_res = temp_res + b_fee[k]
                break
            if b_count == b_order:
                for k in range(j,num):
                    temp_res = temp_res + a_fee[k]
                break
            if a_fee[j] > b_fee[j]:
                temp_res = temp_res + a_fee[j]
                a_count += 1
            elif a_fee[j] < b_fee[j]:
                temp_res = temp_res + b_fee[j]
                b_count += 1
            else:
                temp_res = temp_res + a_fee[j]
        res.append(temp_res)
    return res

res = maxFee()
for i in range(0,len(res)):
    print(res[i])