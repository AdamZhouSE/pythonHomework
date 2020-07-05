def do(string:str):
    count = 0
    if len(string) % 2 == 1:
        return -1
    else:
        available = [True for i in string]
        for i in range(len(string)):
            if not available[i]:
                continue

            if string[i] == '}':
                count += 1
            elif string[i] == '{':
                pass

            last = i+1
            for j in range(i+1,len(string),2):
                if not available[j]:
                    continue
                if string[j] == '}':
                    if string[j-1] == '{' and available[j-1]:
                        available[j] = False
                        available[j-1] = False
                        continue
                    elif string[j-1] == '}':
                        last = j
                        break
                elif string[j] == '{':
                    if j == len(string)-1:
                        last = j
                    else:
                        if string[j+1] == '}':
                            available[j] = False
                            available[j+1] = False
                            continue
                        elif string[j+1] == '{':
                            last = j
            available[i] = False
            available[last] = False
            if string[last] != '}':
                count += 1
    return count

test = int(input())
for i in range(test):
    string = input()
    print(do(string))