T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = int(input())

    tmp = 0
    for i in range(1, len(s) + 1):  # 步长从1到len(s)+1
        for j in range(len(s) - i + 1):
            
            if len(set(s[j:j + i])) == k:
                tmp = max(tmp, i)  # 更新tmp的值
                
    print(tmp)            
