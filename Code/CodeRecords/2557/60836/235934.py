n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    st = string_list[i]
    s_list = list(st)
    j = 1
    while j < len(s_list):
        if s_list[j] == s_list[j-1]:
            del s_list[j]
        else:
            j = j+1
    print("".join([str(n) for n in s_list]))