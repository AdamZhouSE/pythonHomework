tests = int(input())
for i in range(0,tests):
    num = int(input())
    ls = list(map(int,(input().split(' '))))
    tem = sum(ls)
    if tem%3==0:
        print("1")
    else:
        print("0")