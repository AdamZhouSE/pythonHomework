def reverseStr(str):
    s=str[::-1]
    return s
if __name__ == "__main__":
    str=input()
    res=reverseStr(str)
    print(res,end="")