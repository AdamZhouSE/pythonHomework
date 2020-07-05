sub=input()
src=input()
def judge(sub,src):
    for s in sub:
        if s not in src:
            return False
    return True
print(judge(sub,src))