def toInt(a):
    if a == 'I':
        return 1
    elif a == 'V':
        return 5
    elif a == 'X':
        return 10
    elif a == 'L':
        return 50
    elif a == 'C':
        return 100
    elif a == 'D':
        return 500
    elif a == 'M':
        return 1000

def toInt1(b,a):
    if a == 'V':
        return 4
    elif a == 'X':
        return 9
    elif a == 'L':
        return 40
    elif a == 'C':
        return 90
    elif a == 'D':
        return 400
    elif a == 'M':
        return 900

str1 =input()
i = 0
count = 0
while i<len(str1):
    if i == len(str1)-1:
        count += toInt(str1[i])
        i +=1
    elif str1[i] == 'I' and str1[i+1]!= 'I':
        count += toInt1(str1[i],str1[i+1])
        i +=2
    else:
        count += toInt(str1[i])
        i +=1
print(count)