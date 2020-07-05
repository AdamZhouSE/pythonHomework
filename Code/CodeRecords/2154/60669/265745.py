def check():
    for i in range(0,int(len(string)/2)+1):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True
if __name__ == '__main__':
    string = input()
    print(check())