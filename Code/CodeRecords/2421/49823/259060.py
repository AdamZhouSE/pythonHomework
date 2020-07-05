def s(n):
    if not '6' in n:
        print(n)
    else:
        for i in range(len(n)):
            if n[i]=='6':
                print(n[:i]+'9'+n[i+1:])
if __name__ == '__main__':
    s(input())
