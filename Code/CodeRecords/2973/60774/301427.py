s = input()
t = int(input())
total = 0
for i in range(0,t):
    a = input()
    lst = list(set(a))
    ref = [[ch,a.count(ch)] for ch in lst]
    for j in range(0,len(s) - 7):
        temp = s[j:j + 8]
        for item in ref:
            if(temp.count(item[0]) != item[1]):
                break
        else:
            total = total + 1
print(total)