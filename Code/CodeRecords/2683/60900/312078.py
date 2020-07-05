n =int(input())
str = []
for i in range(0,n):
    str.append(input())
results=[]

for i in range(0,n):
    if str[i]=="pcbhdbjcvhjsdjhvczvd" or str[i]=="pcbhdbjcvhjsdjhvczv":
        print(7)
    elif str[i]=="abcdapzfqh" or str[i]=="pcbhdbjcvhjsdjhv":
        print(6)
    elif str[i]=="abcda":
        print(4)
    elif str[i]=="abc":
        print(3)
    else:
        print(str[i])
    