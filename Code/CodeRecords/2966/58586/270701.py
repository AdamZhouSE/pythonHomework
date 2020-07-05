nums=int(input())
for num in range(nums):
    n, m = map(int, input().split(" "))
    target = list(map(str, input().split(" ")))
    src = list(map(str, input().split(" ")))
    ans = []


    def dfs(split, temp, used):
        if len(temp) == 3:
            string = ""
            for p in temp:
                string += "".join(p[0])
            if string == "".join(target):
                for p in temp:
                    ans.append(p[1])
                return True
            else:
                return False
        for i in range(0, 3):
            if i not in used:
                temp.append(split[i])
                used.append(i)
                if dfs(split, temp, used):
                    return True
                used.pop()
                temp.pop()
        return False


    def split():
        for i in range(1, len(src) - 1):
            for j in range(i + 1, len(src)):
                a, b, c = list((src[0:i], [1, i])), list((src[i:j], [i + 1, j])), list(
                    (src[j:], [j + 1, len(src)]))
                if dfs([a, b, c], [], []):
                    return True
        return False


    if split():
        print("YES")
        for p in ans:
            print(*p)
    else:
        print("NO")