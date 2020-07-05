def main():
    word_sources = input().split(" ")
    words = input().split(" ")
    result = True
    able_to_change = [True for i in range(0, len(word_sources))]
    words = sorted(words, key=lambda x: len(x), reverse=True)
    for i in range(0, len(words)):
        be_found = False
        for j in range(0, len(word_sources)):
            if able_to_change[j] and words[i] in word_sources[j]:
                be_found = True
        if not be_found:
            result = False
            break
    if result:
        print("YES", end="")
    else:
        print("NO", end="")


if __name__ == '__main__':
    main()
