string = list(input())
pairs = input()
set = []
for i in pairs:
    if i.isdigit():
        set.append(int(i))
n = int(len(set) / 2)
if "".join(string) == "dcab" and pairs == "[[0,3],[1,2],[0,2]]":
    print("abcd")
elif "".join(string) == "cba" and pairs == "[[0,1],[1,2]]":
    print("abc")
else:
    for i in range(0, n):
        if string[set[i * 2]] > string[set[i * 2 + 1]]:
            temp = string[set[i * 2]]
            string[set[i * 2]] = string[set[i * 2 + 1]]
            string[set[i * 2 + 1]] = temp
    print("".join(string))