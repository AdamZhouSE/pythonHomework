inp = input()
for num in range(0, len(inp)):
    string = inp[:num + 1]
    count = 0
    for length in range(2, len(string)):
        for i in range(0, len(string) - length):
            for j in range(i + 1, i + length):
                if (string[i:i + length] == string[j:j + length]):
                    count = count + length
    print(count)
