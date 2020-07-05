class Solution :
    def kobe(self):
        string = list(input())
        boynum = 0
        girlnum = 0
        i = 0
        while i < string.__len__() :
            if string[i] == 'b':
                if string[i+1] == 'o' :
                    if string[i + 2] == 'y':
                        boynum += 1
                        i += 3
                        continue
                    else:
                        boynum += 1
                        i += 2
                        continue
                else :
                    boynum += 1
                    i += 1
                    continue
            if string[i] == 'o' :
                if string[i+1] == 'y' :
                    boynum += 1
                    i += 2
                    continue
                else :
                    boynum += 1
                    i += 1
                    continue
            if string[i] == 'y':
                boynum += 1
                i += 1
                continue
            if string[i] == 'g':
                if string[i+1] == 'i' :
                    if string[i + 2] == 'r':
                        if string[i + 3] == 'l':
                            girlnum += 1
                            i += 4
                            continue
                        else:
                            girlnum += 1
                            i += 3
                            continue
                    else:
                        girlnum += 1
                        i += 2
                        continue
                else:
                    girlnum += 1
                    i += 1
                    continue
            if string[i] == 'i' :
                if string[i+1] == 'r' :
                    if string[i + 2] == 'l':
                        girlnum += 1
                        i += 3
                        continue
                    else:
                        girlnum += 1
                        i += 2
                        continue
                else :
                    girlnum += 1
                    i += 1
                    continue
            if  string[i] == 'r' :
                if string[i+1] == 'l' :
                    girlnum += 1
                    i += 2
                    continue
                else :
                    girlnum += 1
                    i += 1
                    continue
            if  string[i] == 'l' :
                girlnum += 1
                i += 1
                continue
            i += 1
        print(boynum)
        print(girlnum,end='')
so = Solution()
so.kobe()