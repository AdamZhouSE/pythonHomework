num=int(input())

i=0
while True:
    if i*i>num:
        print(False)
        break
    if i*i==num:
        print(True)
        break
    i=i+1

