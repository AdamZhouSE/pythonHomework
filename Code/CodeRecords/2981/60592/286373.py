nums = list(map(int,input().split()))
str = input()
res = ""
i = 0
while i < len(str):
    if str[i]=='-':
        if ord(str[i-1])>=ord(str[i+1]):
            res+=str[i]
            i+=1
            continue
        else:
            tem = []
            start = ord(str[i-1])+1
            end = ord(str[i+1])
            while start!=end:
                if nums[0]==1:
                    tem.append((chr(start)*nums[1]).lower())
                elif nums[0]==2:
                    tem.append((chr(start)*nums[1]).upper())
                else:
                    tem.append('*'*nums[1])
                start+=1
            if nums[2]==2:
                tem.reverse()
            res+="".join(tem)
            i+=1
    else:
        res+=str[i]
        i+=1
print(res)