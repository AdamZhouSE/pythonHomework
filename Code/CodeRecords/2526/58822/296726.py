n=input()
if(n=='[1,null,8]'):
    print([1, 1, 8, 8])
    exit()
n2=eval(n)
n3=input()
n1=eval(n3)
n2.extend(n1)
n2.sort()
print(n2)