def search(s: str, t: str) -> bool:
    if s == '':
        return True
    flag = False
    index = 0
    for i in range(len(t)):
        if t[i] == s[0]:
            flag = True
            index = i
            break
    return flag and search(s[1:], t[index+1:])


s_string = input()
t_string = input()
print(search(s_string, t_string))