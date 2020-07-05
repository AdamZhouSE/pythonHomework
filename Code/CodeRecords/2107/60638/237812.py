num=int(input())
exp=0
while True:
    n=pow(2,exp)
    if n>num:
        print(False)
        break
    elif n==num:
        print(True)
        break
    exp=exp+1