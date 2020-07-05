def exc(a):
    if a.isdigit():
        return True
    else:
        dot=False
        E=False
        begin=False
        for i in range(len(a)):
            if i!=0 and a[i]=='-':
                return False
            elif a[i]=='e' and E:
                return False
            elif a[i]=='e' and not E:
                E=True
            elif a[i]=='.' and(dot==True or E):
                return False
            elif a[i]=='.':
                dot=True
    return True
             
             
n=input().lstrip()
print(exc(n))