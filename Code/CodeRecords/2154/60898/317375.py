def isCycle(s :str) -> bool:
    if len(s) % 2 == 0:
        one = s[0: int(len(s)/2)]
        sec = s[int(len(s)/2) :]
        if one == sec[::-1]:
            return True
        else:
            return False
    else:
        one = s[0: int(len(s)//2)]
        sec = s[int(len(s)//2) + 1:]
        if one == sec[::-1]:
            return True
        else:
            return False

n = input()
print(isCycle(n))