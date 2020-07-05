def cut2(s):
    results = []
    num = 0

    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            if x == 0:
                results.append(s[i:i + x + 1])
            elif x < 2:
                for j in range(len(s) - x - i):
                    results.append(s[i] + s[j + x + i])
            else:
                for j in range(len(s) - x - i):
                    results.append(s[i:i+x] + s[j + x + i])
    return results

a=input()
b=input()

max=0
temp=0

num1=cut2(a)
num2=cut2(b)
for x in num2:
    if x in num1:
        temp=len(x)
    if(temp>max):
        max=temp
print(len(a)-max)
        
        
        
        
        
        
        
        
        
        