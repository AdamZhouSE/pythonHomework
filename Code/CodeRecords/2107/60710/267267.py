def judge(num):
    num = int(num)
    return True if num == 0 or num & (num - 1) == 0 else False
if __name__ == '__main__':
    a=int(input())
    print(judge(a))