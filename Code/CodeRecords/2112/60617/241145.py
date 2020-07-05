def main():
    Array=input().split(",")
    Array=list(map(int, Array))
    Array.sort()
    maxNum=max(Array)
    for Num in range(0, maxNum):
        if Num not in Array:
            print(Num)

if __name__ == '__main__':
    main()