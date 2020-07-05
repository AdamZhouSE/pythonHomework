num=int(input())
b=False
for i in range(1,num):
    if i*i==num:
        print(True)
        b=True
        break
if not b:
    print(False)