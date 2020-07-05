def Test():
    num=eval("["+input()+"]")
    num.sort()
    for i in range(0,len(num)+1):
        if(i in num):
            continue
        else:
            print(i)
            break
if __name__ == "__main__":
    Test()