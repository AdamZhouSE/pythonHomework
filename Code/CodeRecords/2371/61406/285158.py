T = int(input())
for a in range(0,T):
    source = input()
    string = ""
    for i in source:
        if i.isdigit():
            string += i
        if i.isalpha():
            if ord('a')<=ord(i)<=ord('z'):
                string += chr(ord(i)-ord('a')+ord('A'))
            else:
                string += i
    list1=list(reversed(string))
    reverse = ""
    for j in list1:
        reverse+=j
    if reverse==string:
        print("YES")
    else:
        print("NO")
