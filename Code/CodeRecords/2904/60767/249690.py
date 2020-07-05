def reverse(num):
    temp = []
    for i in num:
        temp.append(i)
    if(temp[0]=="-"):
        temp.remove("-")
        temp.reverse()
        res = "-"

    else:
        temp.reverse()
        res = ""
    j = 0
    while (temp[j]=="0"):
        j+=1
    for i in range(j,len(temp)):
        res += temp[i]
    return (res)

num = input()
if(num=="0"):
    print(0)
else:
    print(reverse(num))

