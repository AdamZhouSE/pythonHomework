if __name__ == '__main__':
    S = input()
    T = input()
    print("".join(sorted(list(T), key=lambda x: S.find(x))))