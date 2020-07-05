a=int(input())
bstr=input()
b=bstr.split(',')

r = 1
for i in b:
    r = pow(r, 10, 1337) * pow(a,int(i), 1337) % 1337
print(r)
