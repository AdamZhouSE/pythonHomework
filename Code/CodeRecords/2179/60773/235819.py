def findMax(s1,s2):
    max=0
    m=min(len(s1),len(s2))
    for i in range(len(s1)):
        if s1[i]==s2[0]:
            for j in range(m-i):
                if s1[i+j] != s2[j]:
                    break
            if j+1>max:
                max=j+1
    return max

start = input();
num = int(start[2])
s = input()
list=[]
for i in range(num):
    list.append(input())
for i in range(num):
    num1=int(list[i][0])
    num2=int(list[i][2])
    num3=int(list[i][4])
    num4=int(list[i][6])
    str1=s[num1:num2+1]
    str2=s[num3:num4+1]
    print(findMax(str1,str2))
