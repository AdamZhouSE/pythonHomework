def shuzi(a):
    i=0
    while i<len(a)//2:
        if a[i]!=a[len(a)-1-i]:
            return False
        i+=1
    return True
a=input()
print(shuzi(a))