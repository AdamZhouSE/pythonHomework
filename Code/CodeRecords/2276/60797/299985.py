class Solution:
    def find(self, r, c, r0, c0):
        re = []
        count = 0
        direct = 1
        path = 1
        re.append([r0, c0])
        count += 1
        while count < r * c:
            if direct % 4 == 1:
                if path==1:
                    if 0<=r0<r and 0<=c0+1<c:
                        re.append([r0, c0 + 1])
                        count += 1
                else:
                    for i in range(1, path):
                        if 0<=r0<r and 0<=c0+i<c:
                            re.append([r0, c0 + i])
                            count += 1
                        else:
                            break
                c0 = c0 + path
                direct += 1
            elif direct % 4 ==2:
                for i in range(1,path):
                    if 0 <= r0+i < r and 0 <= c0 < c:
                        re.append([r0+i,c0])
                        count += 1
                    else:
                        break
                r0 = r0 + path
                direct += 1
                path += 1
            elif direct% 4==3:
                for i in range(1,path):
                    if 0 <= r0 < r and 0 <= c0 - i < c:
                        re.append([r0,c0 -i])
                        count += 1
                    else:
                        break
                c0 = c0 -path
                direct += 1
            else:
                for i in range(1,path):
                    if 0 <= r0-i < r and 0 <= c0 < c:
                        re.append([r0-i,c0])
                        count+=1
                    else:
                        break
                r0 = r0-path
                direct +=1
                path +=1
        return re


if __name__ == '__main__':
    r = int(input())
    c = int(input())
    r0 = int(input())
    c0 = int(input())
    s = Solution()
    re = s.find(r, c, r0, c0)
    print(re)
