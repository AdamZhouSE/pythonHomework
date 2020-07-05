a=int(input())
b=input().strip('[').strip(']').split(',')
num=int(''.join(b))
pro=1
for i in range(num):
    pro=pro*a
result=pro%1337
print(result)
