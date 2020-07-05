def compare(l1, l2):
    if (l1[0]-l2[0])*(l1[1]-l2[1]) < 0:
        return True
    else:
        return False


def function(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if compare(l[i], l[j]):
                return True
    return False


n = int(input())
string = []
for i in range(n):
    string.append(input())

l = [[]for i in range(n)]
for i in range(n):
    for j in range(len(string[0])):
        if string[i][j].isdigit():
            l[i].append(int(string[i][j]))

if function(l):
    print("Happy Alex")
else:
    print("Poor Alex")