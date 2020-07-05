string = input()
lst = input().split()
if lst[0] == "D":
    print(string.replace(lst[1],'',1))
elif lst[0] == "I":
    print(string.replace(lst[1],lst[2]+lst[1],1))
elif lst[0] == "R":
    print(string.replace(lst[1],lst[2]))