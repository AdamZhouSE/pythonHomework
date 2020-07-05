n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    s_list = list(string_list[i])
    result=True

    for m in range(len(s_list)):
        j = m+1
        while j < len(s_list):
            if s_list[m] == s_list[j]:
                result=False
                break
            else:
                j = j+1

    if result:
        print(1)
    else:
        print(0)