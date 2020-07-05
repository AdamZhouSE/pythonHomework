class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty: # 相等了不能再进行取余了，直接break看看是不是和初始相等即可
                break
            elif tx > ty: # tx大，减tx
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0 # 此时ty == sy了，到边界了，不可以减了，只需要看tx和边界的差值能不能整除sy了
                    # 对的，你不用问，这个ty可以改成sy的
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy # 上面搞完没return，看看是不是和初始相等即可

if __name__ == "__main__":
    # sx = 1
    # sy = 1
    # tx = 3
    # ty = 5
    s = Solution()
    print(s.reachingPoints(int(input()), int(input()), int(input()), int(input())))

