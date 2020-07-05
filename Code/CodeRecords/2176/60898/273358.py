s1 = input()
l1 = len(s1)
s2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = ""
for i in range(52):
    for j in range(l1):
        if s1[l1-j-1]==s2[i]:
            b=str(l1-j)
            a=a+b+" "
print(a)  