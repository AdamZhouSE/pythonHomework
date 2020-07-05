#质数
t=int(input())
for nn in range(t):
    num=int(input())
    num=num+2
    flag='Yes'
    for i in range(2,num):
        if num % i ==0 :
            flag = 'No'
            break
    print(flag)
      