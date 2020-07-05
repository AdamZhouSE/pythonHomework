s = input()
result = 0
i = 0
while(i<len(s)):
    if s[i] == "I":
        if i<len(s)-1 and s[i+1] == "V" :
            result += 4
            i+=1
        elif i<len(s)-1 and s[i+1] == "X":
            result += 9
            i += 1
        else:
            result += 1
        i+=1
        continue
    if s[i] == "V":
        result += 5
        i += 1
        continue
    if s[i] == "X":
        if i<len(s)-1 and s[i+1] == "L":
            result += 40
            i += 1
        elif i<len(s)-1 and s[i+1] == "C":
            result += 90
            i += 1
        else:
            result += 10
        i += 1
        continue
    if s[i] == "L":
        result += 50
        i += 1
        continue
    if s[i] == "C":
        if i<len(s)-1 and s[i+1] == "D":
            result += 400
            i += 1
        elif i<len(s)-1 and s[i+1] == "M":
            result += 900
            i += 1
        else:
            result += 100
        i += 1
        continue
    if s[i] == "D":
        result += 500
        i += 1
        continue
    if s[i] == "M":
        result += 1000
        i += 1
        continue
print(result)