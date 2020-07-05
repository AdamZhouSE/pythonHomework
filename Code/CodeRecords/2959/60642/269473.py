str1 = input()
str2 = input()
times = 0
for i in range(1,len(str1)+1):
    jjj = len(str1)-i+1
    for j in range(len(str1)-i+1):
        sss = str1[j:j+i]
        if(str2.count(str1[j:j+i])!=0):
            times+=str2.count(str1[j:j+i])
print(times)