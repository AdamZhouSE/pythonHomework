str=input()
length=len(str)
begin=length
first=0
end=length
for i in range(length):
    if str[i]=="-" or str[i]=='+' or ('0'<=str[i] and str[i]<='9'):
        begin=i
        break
for i in range(length):
    if str[i]!=' ':
        first=i
        break
for i in range(begin+1,length):
    if ('9'<str[i] or str[i]<'0'):
        end=i
        break
res=int(str[begin:end])
if res>2147483648:
    res=2147483648
if res<-2147483648:
    res=-2147483648
if begin>first:
    res=0
print(res)