class Solution:
    def find(self, s):
        x,y=0,0
        drc = 1
        for times in range(4):
            for i in range(len(s)):
                if drc == 1:
                    if s[i]=='G':
                        y += 1
                    elif s[i]=='L':
                        drc = 4
                    else:
                        drc = 2
                elif drc==2:
                    if s[i]=='G':
                        x += 1
                    elif s[i]=='L':
                        drc = 1
                    else:
                        drc = 3
                elif drc==3:
                    if s[i]=='G':
                        y -= 1
                    elif s[i]=='L':
                        drc = 2
                    else:
                        drc = 4
                else:
                    if s[i]=='G':
                        x -= 1
                    elif s[i]=='L':
                        drc = 3
                    else:
                        drc = 1
                if x==0 and y==0:
                    return 'True'
        return 'False'


if __name__ == '__main__':
    data = input()
    s = Solution()
    re = s.find(data)
    print(re)
