i1=input().split("+")
i2=input().split("+")
i1[1]=i1[1][:-1]
i2[1]=i2[1][:-1]
i1=[int(x) for x in i1]
i2=[int(x) for x in i2]
real=i1[0]*i2[0]-i1[1]*i2[1]
imag=i1[0]*i2[1]+i1[1]*i2[0]
print("{}+{}i".format(real,imag))