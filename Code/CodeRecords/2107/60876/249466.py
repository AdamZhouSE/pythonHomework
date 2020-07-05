num=int(input())
jud=True
while num!=1:
    if num%2!=0:
        jud=False
        break
    num=num//2
print(jud)