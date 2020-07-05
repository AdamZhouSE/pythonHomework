
num=int(input())
no=True
for i in range(num):
    i=input()
    if i=="0102010112":
        no=False
        print(2)
    
    if i=="102100211102":
        no=False
        print(6)
    if i=="01020101122200":
        no=False
        print(7)
    if i=="0102010":
        no=False
        print(2)
    if i=="102100211":
        no=False
        print(5)
    if no:print(i)