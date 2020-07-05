def shuzi(a):
    if a==1:
        return True
    else:
        while a>3 and a%3==0:
            a=a/3
        return a==3
a=int(input())
print(shuzi(a))