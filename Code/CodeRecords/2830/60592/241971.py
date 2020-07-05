pre = list(map(int,input().split(' ')))
num1 = pre[0]
num2 = pre[1]
ls = list(map(int,input().split(' ')))
res = 0
for i in range(0,num2):
    res+=(ls[i])*(pow(num1,num2-1-i)%2)
    res%=2
if res == 1:

    print("odd")
else:
    print("even")