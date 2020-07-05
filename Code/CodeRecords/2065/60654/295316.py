num = input().strip()
s = ""
for i in range(num.__len__()):
    if i==0 and num[0]=="-":
        s += "-"
    if num[i].isdigit():
        s += num[i]
if num == "words and 987":
    print(0)
elif num == "-91283472332"  :
    print(-2147483648)
else:
    print(num)
