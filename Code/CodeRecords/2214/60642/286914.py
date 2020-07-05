str1 = input().split('+')
str2 = input().split('+')
ima1 = int(str1[1][0:-1])
ima2 = int(str2[1][0:-1])
out = [0,0]
out[0]=int(str1[0])*int(str2[0])-ima1*ima2
out[1]=int(str1[0])*ima2+int(str2[0])*ima1
print(str(out[0])+'+'+str(out[1])+'i')