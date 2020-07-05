

s = input()
count = 0
checked = set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        temp = s[i:j]
        re = True
        con = 0
        for i in range(len(temp)-1):
            if temp[i] != temp[i+1]:
                con += 1
        if (con == 1 or con == 0) and temp not in checked:
            checked.add(temp)
            count += 1
            
print(count)