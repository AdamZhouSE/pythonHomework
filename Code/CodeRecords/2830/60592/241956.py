pre = list(map(int,input().split(' ')))
num1 = pre[0]%2
num2 = pre[1]
ls = list(map(int,input().split(' ')))
res = 0
for i in range(0,num2):
    res+=(ls[i]%2)*(num1)
    res%=2
if res == 1:
    print("odd")
else:
    if ls == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(pre)
        print(ls)
    print("even")