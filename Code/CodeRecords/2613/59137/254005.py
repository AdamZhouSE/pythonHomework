def s19():

    def print19(this, number, flag):
        this = int(this)
        number = int(number)
        ans = []

        for j in range(number):
            ans.append(this)
            this = this + 2

        for s in ans[0:len(ans)-1]:
            print(str(s) + " ", end="")

        if flag == 1:
            print(str(ans[len(ans)-1]), end="")
        else:
            print(str(ans[len(ans)-1]) + " ", end="")

        return ans[len(ans)-1]

    num = int(input())
    for x in range(num):

        n = int(input())
        count = 0
        now = 1
        last = 0
        flag = 0

        while count + now <= n:
            if count + now == n:
                flag = 1
            last = print19(last+1, now, flag)
            count = count + now
            now = now + 1

        if count < n:
            flag = 1
            last = last + 1
            print19(last, n-count, flag)

        print()


s19()
