n=int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    s_int = int(string_list[i])

    if s_int%2==1:
        print("Player A")
    else:
        print("Player B")