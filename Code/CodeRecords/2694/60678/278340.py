def hasRepeated(substr, string):
    if string.find(substr) != string.rfind(substr):
        return True
    return False


def missionSearch():
    string = input()
    for length in range(len(string) - 1, 1, -1):
        for start in range(0, len(string) - length + 1):
            substr = string[start:start + length]
            if hasRepeated(substr, string):
                print(substr)
                return
    print("")
    return


missionSearch()