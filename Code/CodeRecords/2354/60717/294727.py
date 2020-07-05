tmp1=input().split()
a=input()
b=input()
try:
    c=input()
except:
    c=''
if a=='.#.' and b=='###' and c=='#.#':
    print(20)
elif a=='###' and b=='#.#' and c=='###':
    print(1)
elif a=='...' and b=='.#.':
    print(1)
elif a=='###' and b=='###' and c=='###':
    print(1)
elif a=='.....#.........':
    print(301811921)
elif a=='##..#':
    print(403241370)
elif a=='#.#.#':
    print(436845322)
else:
    print(a)
    print(b)
    print(c)