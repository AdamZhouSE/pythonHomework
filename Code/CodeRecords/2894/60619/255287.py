length = int(input())
string = list(input())
haveAlter = False
if length == 2:
    if ''.join(string) != "KV":
        print(1, end="")
    else:
        print(0, end="")
else:
    for i in range(length-2):
        if string[i] == "V" and string[i+1] == "V" and string[i+2] != "K" and not haveAlter:
            string[i+1] = "K"
            haveAlter = True
            break
    if not haveAlter:
        j = length - 1
        while j >= 2:
            if string[j] == "K" and string[j-1] == "K" and string[j-2] != "V" and not haveAlter:
                string[j-1] = "V"
                haveAlter = True
                break
            j -= 1
    print(''.join(string).count("VK"), end="")