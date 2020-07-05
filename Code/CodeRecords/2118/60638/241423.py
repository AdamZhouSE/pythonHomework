num=int(input())
exp=1
while True:
    if num==exp:
        print(True)
        break
    elif num<exp:
        print(False)
        break
    exp=exp*3