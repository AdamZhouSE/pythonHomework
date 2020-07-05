a = int(input())
b = input().split(',')

e = 0
for i in b:
    e = e*10 +int(i)
print(pow(a,e,1337))