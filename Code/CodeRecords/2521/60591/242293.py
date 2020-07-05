def a(x):
    return dict[x]

temp = list(input()[1:-1].split(","))
dict = {}
string = []
for m in temp:
    if m in dict:
        dict[m] += 1
    else:
        dict[m] = 1
    string.append("")
    string.append("")
i = 0
j = 1
dict_keys = list(dict.keys())
dict_keys.sort(reverse=True,key=a)
for m in range(len(dict)):
    if(i < j):
        while(dict[dict_keys[m]] > 0):
            dict[dict_keys[m]] -= 1
            string[i] = dict_keys[m]
            i = i + 2
    else:
        while(dict[dict_keys[m]] > 0):
            dict[dict_keys[m]] -= 1
            string[j] = dict_keys[m]
            j = j + 2

print("[" + ", ".join(list("".join(string))) + "]")