wds = []


def ins(word):
    global wds
    wds.append(word)
    
    
def dele(word):
    global wds
    if word in wds:
        wds.remove(word)

    
def sea(word):
    print("YES" if wds.count(word) else "NO")
    
    
def prefix(pre):
    cnt = 0
    for word in wds:
        if word.startswith(pre):
            cnt += 1
    print(cnt)
    
    
if __name__ == "__main__":
    m = int(input())
    while m:
        cmd = input().split( )
        op = int(cmd[0])
        src = cmd[1]
        if op==1:
            ins(src)
        elif op==2:
            dele(src)
        elif op==3:
            sea(src)
        else:
            prefix(src)
        m -= 1       