sub = input()
source = input()

def check(sub,source):
    idx = 0
    for i,s in enumerate(source):
        if sub[idx] == s:
            idx += 1
    if idx == len(sub):
        return True
    else:
        return False

print(check(sub,source))
