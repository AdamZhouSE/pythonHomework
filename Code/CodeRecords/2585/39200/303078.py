start = input()
end = input()
i, j = 0, 0
flag = 1
if not start == end:
    while i < len(start) and j < len(end):
        while i < len(start)-1 and start[i]=="X":
            i += 1
        while j < len(end)-1 and end[j]=="X":
            j += 1
        if not start[i] == end[j]:
            flag = 0
        if (start[i]=="L" and i<j) or (end[j]=="R" and i>j):
            flag = 0
        i += 1
        j += 1
if flag:print("True")
else:print("False")
