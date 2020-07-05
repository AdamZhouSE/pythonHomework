result="False"
a=int(input())
for i in range(1,1000000):
    if i*i==a:
        result="True"
        break
    if i*i>a:
        break
print(result)