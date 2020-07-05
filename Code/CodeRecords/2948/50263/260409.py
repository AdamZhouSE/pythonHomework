string1 = input()
string2 = ''
st = int(input())
list1 = []
list2 = []
def plus_str(string):
    a = string
    b = string[1:len(string)]
    c = ''
    for i in range(len(b)):
        c = c + str((int(a[i]) + int(b[i])) % 10)
    return c
    
for i in range(len(string1)):
    list1.append(st + (ord(string1[i]) - ord('A')))
for j in range(len(list1)):
    string2 = string2 + str(list1[j])
while(int(string2)>100):
    string2 = plus_str(string2)
if string2[0] == '0':
    string2 = string2[1:]
print(string2,end='')