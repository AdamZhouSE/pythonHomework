
def is_reverse(string: str) -> bool:
    return string == string[::-1]


s = input()
ls = [list(input().split()) for i in range(0, int(input()))]
for sub_ls in ls:
    if sub_ls[0] == 1:
        s += sub_ls[1]
    elif sub_ls[0] == 2:
        s = sub_ls[1][::-1] + s
    else:
        count = 0
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                s_slice = s[j:j + i]
                if is_reverse(''.join(s_slice)):
                    count += 1
        print(count)