num = int(input())
for i in range(num):
    ans = []
    pw = input()
    li = []
    index = 0
    while index != len(pw):
        st = ""
        t = ""
        if pw[index] == "]":
            li.pop()
            st = "".join(ans)
            ans.clear()
            t = st
            for j in range(int(li[len(li)-1])-1):
                st = st + t
            li.pop()
            if li == []:
                ans.append(st)
                index = index + 1
                print(ans[0])
            else:
                while li[len(li)-1] != "[":
                    st = li.pop() + st
                index = index + 1
                ans.append(st)
        else:
            while pw[index] != "]":
                li.append(pw[index])
                index = index + 1
            while li[len(li)-1] != "[":
                st = li.pop() + st
            li.pop()
            t = st
            for j in range(int(li[len(li)-1])-1):
                st = st + t
            li.pop()
            if li == []:
                ans.append(st)
                index = index + 1
                print(ans[0])
            else:
                while li[len(li) - 1] != "[":
                    st = li.pop() + st
                index = index + 1
                ans.append(st)