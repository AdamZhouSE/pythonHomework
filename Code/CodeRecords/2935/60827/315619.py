str1 = input()
i1 = str1.find("Q",0,len(str1))
str1 = str1[i1:]
x=0
c= 0
for i in range(len(str1)-2):

    i1 = str1.find("Q", x, len(str1))
    i = i1+1
    x= i1+1
    if i1 == -1:
        break
    else :
        j = i1 +1
        for n in range (len(str1)-1-j):
            i2 = str1.find("A",j,len(str1))
            j=i2+1
            if i2 == -1 :
                break
            else:
                k = i2+1
                for m in range (len(str1)-k):
                    i3 = str1.find("Q",k,len(str1))
                    k=i3+1
                    if i3 == -1:
                        break
                    else:
                        c = c+1
print(c,end='')


