def calZero(n):
    count_5 = 0
    while n > 0:
        count_5 += int(n/5)
        n = int(n/5)
    return count_5

if __name__ == "__main__":
    n = int(input())
    print(calZero(n))