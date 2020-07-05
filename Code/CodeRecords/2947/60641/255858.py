def main():
    num_of_instrument = int(input())
    string = input()
    instruments = []
    for i in range(0, num_of_instrument):
        instrument = input().split(" ")
        instruments.append(instrument)

    for i in range(0, num_of_instrument):
        instrument = instruments[i]
        if instrument[0] == "1":
            string = string + instrument[1]
            print(string)
        elif instrument[0] == "2":
            string = string[int(instrument[1]):int(instrument[1]) + int(instrument[2])]
            print(string)
        elif instrument[0] == "3":
            string = string[:int(instrument[1])] + instrument[2] + string[int(instrument[1]):]
            print(string)
        elif instrument[0] == "4":
            for j in range(0, len(string) - len(instrument[1]) + 1):
                if instrument[1] == string[j:j + len(instrument[1])]:
                    print(j)
                    break


if __name__ == "__main__":
    main()
