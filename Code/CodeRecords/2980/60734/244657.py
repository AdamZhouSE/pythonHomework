string = input()
lst = input().split()
if lst[0] == "D":
    print(string.replace(lst[1],'',1))
elif lst[0] == "I":
    string = string[::-1].replace(lst[1],lst[1]+lst[2],1)
    print(string[::-1])
elif lst[0] == "R":
    print(string.replace(lst[1],lst[2]))
else:
    print('no exist')
    print(string)