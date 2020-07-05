def main():
    n = int(input())
    for i in range(0, n):
        HP_1, HP_2, HP_prince = map(int, input().split(" "))
        j = HP_1
        k = HP_2
        while HP_prince > 1:
            if HP_1 % HP_prince == 0:
                HP_1 -= 1
            if HP_2 % HP_prince == 0:
                HP_2 -= 1
            HP_prince -= 1
        print(str(j - HP_1) + " " + str(k - HP_2))


if __name__ == '__main__':
    main()
