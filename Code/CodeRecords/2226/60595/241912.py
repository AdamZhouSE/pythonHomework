def Test():
    up=int(input())
    down=int(input())
    line=[]
    for i in range(up,down+1):
        if(isDiv(i)):
            line.append(i)
    print(line)

def isDiv(x):
    for word in str(x):
        if(word=="0"):
            return False
        else:
            if(x%int(word)!=0):
                return False
    return True
if __name__ == "__main__":
    Test()