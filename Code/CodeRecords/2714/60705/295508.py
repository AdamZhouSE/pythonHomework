if __name__ == '__main__':
    words = []
    while True:
        try:
            words.append(input())
        except EOFError:
            break
    print(words)