def transfer(n:int):
    # 2、采用python自带了方法bin函数，比如bin(12345)
    # 返回字符串'0b11000000111001', 这个时候在把0b去掉即可:
    # >>> bin(12345).replace('0b', '')
    # '11000000111001'
    # 3、也可以采用字符串的format方法来获取二进制：
    # >>> "{0:b}".format(12345)
    # '11000000111001'
    binS=bin(n).replace("0b","")
    return binS

def solution(n):
    binStr=transfer(n)
    for i in range(len(binStr)-1):
        if binStr[i]==binStr[i+1]:
            return False
        else:
            continue
    return True


if __name__=="__main__":
    n=int(input())
    ans=solution(n)
    print(ans)