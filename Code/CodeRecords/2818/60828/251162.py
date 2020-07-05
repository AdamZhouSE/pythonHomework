def h_3_4():
    s = input().split(" ")
    n = int(s[0])
    x = int(s[1])
    ci = list(map(int,input().split(" ")))
    for i in range (0,n):
    #从小到大
        for j in range (i,n):
            if(ci[i]>ci[j]):
                temp = ci[i]
                ci[i] = ci[j]
                ci[j] = temp
    sum = 0
    for i in range(0,n):
        sum += x*ci[i]
        if(x>=2):
            x -= 1
    print(sum)



if __name__ == '__main__':
    # h_3_1()
    # h_3_2()
    # h_3_3()
    h_3_4()