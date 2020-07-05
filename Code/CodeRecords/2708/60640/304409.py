"""
存储每个房间实验时的一群人，后面的实验时如果该房间人没有变，则不加分
"""


class Solution:

    def get_points(self, p, r, q, operations):
        rooms = [[] for _ in range(r)]
        rooms[0] = [x for x in range(1, p+1)]
        after_op = []
        points = []
        for op in operations:
            if op[0] == 'C':
                for room in rooms:
                    if op[1] in room:
                        room.remove(op[1])
                        break
                rooms[op[2]-1].append(op[1])
            else:
                points.append(Solution().do_lab(rooms, op[1], op[2], after_op))
        return points

    def do_lab(self, ro, l, r, after):
        pointer = 0
        for i in range(l-1, r):
            if not after.__contains__(ro[i]):
                pointer += len(ro[i])
                after.append([ro[i][x] for x in range(0, len(ro[i]))])
        return pointer


if __name__ == "__main__":
    inp = input().split(" ")
    N, M, Q = int(inp[0]), int(inp[1]), int(inp[2])
    opera = []
    for ii in range(0, Q):
        inp = input().split(" ")
        opera.append([inp[0], int(inp[1]), int(inp[2])])
    s = Solution()
    res = s.get_points(N, M, Q, opera)
    for re in res:
        print(re)
