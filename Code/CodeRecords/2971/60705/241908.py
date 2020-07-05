string = input()
dic = {}
for i in range(0, len(string)):
    dic[string[len(string) - 1 - i:len(string)]] = len(string) - i
l = sorted(dic.keys(), reverse=False)
for i in range(0, len(l)):
    print(dic[l[i]], end=" ")
