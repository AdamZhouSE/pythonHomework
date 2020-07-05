num = int(input())
result = True
transtwo = False
transthree = False
transfive = False
trans = transtwo and transthree and transfive
while trans:
    if num%2!=0:transtwo = True
    else: num //=2
    if num%3!=0:transthree = True
    else: num //=3
    if num%5!=0:transfive = True
    else: num //=5
    trans = transtwo and transthree and transfive
for i in range(6,num):
    if num%i==0:
        result = False
        break
print(result)