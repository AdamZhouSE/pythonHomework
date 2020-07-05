num=int(input())
for i in range(10):
    if pow(2,i)>num:
        print(num^(pow(2,i)-1))
        break