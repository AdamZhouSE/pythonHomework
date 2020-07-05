src=input()
src=list(src)


def judge(src):
    l=len(src)
    if l<=1:
        return True
    return src[0]==src[-1] and judge(src[1:l-1])


print(judge(src))
 