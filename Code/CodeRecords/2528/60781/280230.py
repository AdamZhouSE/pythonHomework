str1=input()
len=len(str1)
str1=str1[1:len-1]
str1=str1.split(',')
str1=list(map(int,str1))
str1.sort()
print(str1)