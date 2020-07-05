num = int(input())
init = input()
source = ""
for x in init:
    if x!=' ':
        source=source+x
result = ""
end = 0
for x in range(1,len(source)+1):
    end =source.index(str(x))
    result=result+str(end+1)+" "
    #翻转从x到end的字符串
    temp=''.join(reversed(source[x-1:end+1]))
    source=source[0:x-1]+temp+source[end+1:]
print(result[0:len(result)-1],end=' ')