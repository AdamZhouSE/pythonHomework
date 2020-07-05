str = input()
num = int(input())
count = 0
max = 1
i = 0
j = 0
mark = [0]
while i < len(str) and j < len(str):
    i = mark[0]
    j = i
    mark.pop(0)
    re = num
    count = 0
    while j<len(str) and str[j]==str[i]:
        j+=1
        count+=1
        while j<len(str) and str[j]!=str[i] and re > 0:
            mark.append(j)
            if re>0:
                j+=1
                re-=1
                count+=1
    if count > max:
        max = count
print(max)