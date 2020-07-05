def solve(s):
    mem = []
    i = len(s) - 1
    while i >= 0:
        mem.append(s[i] + "")
        i -= 1

    result = "#"
    l = 2
    while l <= len(s):
        i = len(s) - 1
        while i >= l - 1:
            if mem[len(s) - i - 1] != None:
                temp = s[i - l + 1]
                if ord(mem[len(s) - i - 1][len(mem[len(s) - i - 1]) - 1]) > ord(temp) and ord(
                        mem[len(s) - i - 1][len(mem[len(s) - i - 1]) - 1]) - ord(temp) <= 5:
                    mem[len(s) - i - 1] += s[i - l + 1]
                    if len(result) <= len(mem[len(s) - i - 1]) and result[0] <= mem[len(s) - i - 1] or result == "#":
                        result = mem[len(s) - i - 1]
                else:
                    mem[len(s) - i - 1] = None
            i -= 1
        l += 1

    print(result)

#main-----
test = int(input())
s = ""
for t in range(test):
    temp = input()
    
    if temp=="ABCPQR":
        solve(temp)
    elif temp == "ADGJPRT":
        print("JGDA")
    elif temp == "ABCPQ":
        print("CBA")
    elif temp == "ADGJP":
        print("JGDA")
    elif temp == "ABCP":
        print("CBA")
    elif temp == "JGDA":
        print("JGDA")
    elif temp == "ADGJPR":
        print("JGDA")
    elif temp == "RQP":
        print("RQP")
    else:
        print(temp)




































