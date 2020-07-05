def positive(string,num):
    l = list(string)
    res = 0
    for i in range(1, len(l)):
        if l[:i].count(string[i]) != 0:
            res = res + 1
    return len(string)-res <=num



def findnum(string,origin):
    num = 0
    for i in range(len(origin)-len(string)+1):
        if string == origin[i:i+len(string)]:
            num = num + 1
    return num


string = input()
maxLetters = int(input())
minsize = int(input())
maxsize = int(input())
max = 0
for i in range(minsize,maxsize):
    for k in range(len(string)-i+1):
        s = string[k:k+i]
        if positive(s,maxLetters):
            num = findnum(s,string)
            if num > max:
                max = num
print(max)