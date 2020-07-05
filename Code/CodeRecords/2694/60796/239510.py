str=input()
max=0
maxstring=""
for i in range(0,len(str)):
    if str.count(str[i:i+1])>1:
        max=1#有字符在字符串里重复出现过
        break
if max>0:
    for i in range(len(str) - 1):
        j = i + 1
        while j <= len(str) - 1:
            length = j + 1 - i
            substring = str[i:j + 1]
            if length>max:
                if str[i+1:].count(substring)>0:#出现重复，并且包括重叠字符串的现象
                    maxstring=substring
                    max=length
            j=j+1
      
print(maxstring)

