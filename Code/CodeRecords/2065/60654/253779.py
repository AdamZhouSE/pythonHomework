num = list(input())
s = ""
for i in num:
    if i == " ":
        del i
for i in range(num.__len__()):
    if i==0 and num[0]=="-":
        s += "-"
    if num[i].isdigit():
        s += num[i]
print(s)
