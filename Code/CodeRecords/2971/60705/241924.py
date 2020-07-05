string = input()
dic = {}
for i in range(0, len(string)):
    dic[string[len(string) - 1 - i:len(string)]] = len(string) - i
li = sorted(dic.keys(), reverse=False)
for i in range(0, len(li)):
    print(dic[li[i]], end=" ")
