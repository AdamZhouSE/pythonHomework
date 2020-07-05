a = input()
b = input()
def strToList(s):
    s = s[1:-1]
    s = s.split(",")
    arr = []
    for i in s:
        if i == 'null' or i == '':
             pass
        else:
           arr.append(int(i))
    return arr
     
a = strToList(a)
b = strToList(b)
print(sorted(a+b))