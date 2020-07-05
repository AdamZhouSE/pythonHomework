#n-2是质数
#1,3,7,9,13,19,27
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
      