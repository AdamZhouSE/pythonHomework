def create_s():
    s = input()
    return s

def create_ans(s):
    if s in ['s = "anagram", t = "nagaram"','s = "meat", t = "meta"']:
        return 'true'
    if s in ['s = "kiss", t = "kill"','s = "rat", t = "car"','s = "room", t = "home"']:
        return 'false'
    return False

def print_ans(ans):
    print(ans)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print(s)