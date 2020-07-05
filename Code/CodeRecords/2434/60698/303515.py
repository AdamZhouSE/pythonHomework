def test():
    nmc=input().split()
    n=int(nmc[0])
    m=int(nmc[1])
    c=int(nmc[2])
    sounds=input().split()
    sounds=list(map(int,sounds))
    exist=False
    for i in range(0,len(sounds)-m+1):
        minimum=min(sounds[i:i+m])
        maximum=max(sounds[i:i+m])
        if maximum-minimum<=c:
            print(i+1)
            exist=True
    if not exist:
        print('NONE',end='')
test()